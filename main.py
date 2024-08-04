import httpx
import bs4
import re
import json
import random
from typing import List, Dict, Union

class TopGamesObject(object):
    def __init__(self, jsresult: dict) -> None:
        self.data = jsresult

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)

    @property
    def pagination(self) -> dict:
        return self.data['pagination']
    
    @property
    def total_games(self) -> int:
        return self.data['total']
    
    def getGames(self) -> List[Dict]:
        return self.data['items']
    
    def getRandomGame(self):
        return TopGamesData(random.choice(self.getGames()))
    
    def getGameById(self, game_id: str):
        for item in self.getGames():
            if item['id'] == game_id:
                return TopGamesData(item)
            
        return {}
    
class TopGamesData(object):
    def __init__(self, itemresult: dict) -> None:
        self.data = itemresult

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)

    @property
    def id(self) -> str:
        return self.data['id']
    
    @property
    def name(self) -> str:
        return self.data['name']
    
    @property
    def slug(self) -> str:
        return self.data['slug']
    
    @property
    def cover(self) -> str:
        return self.data['cover']
    
    @property
    def status(self) -> str:
        return self.data['status']
    
    def getGameThumbLabels(self) -> List[str]:
        return self.data['gameThumbLabels']
    
    def getCategoryName(self) -> str:
        return self.data['categoryName']
    
    def getGameAverageRating(self) -> Union[float, int]:
        return self.data['gameAverageRating']
    
    def getVideos(self) -> dict:
        return self.data['videos']
    
    def isHttps(self) -> bool:
        return self.data['https']
    
    def isMobileFriendly(self) -> bool:
        return self.data['mobileFriendly']
    
    def isAndroidFriendly(self) -> bool:
        return self.data['androidFriendly']
    
    def isIosFriendly(self) -> bool:
        return self.data['iosFriendly']
    
    def isStaffPicked(self) -> bool:
        return self.data['isStaffPicked']
    
    def isInstant(self) -> bool:
        return self.data['isInstant']
    
class HomePageGamesObject(object):
    def __init__(self, jsresult: dict) -> None:
        self.data = jsresult

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)

    def getRandomPage(self) -> dict:
        return random.choice(self.data)
    
    def getPageById(self, page_id: str):
        for item in self.data:
            if item['id'] == page_id:
                return HomePageGamesData(item)
            
        return {}
    
class HomePageGamesData(object):
    def __init__(self, itemresult: dict) -> None:
        self.data = itemresult

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)
    
    @property
    def id(self):
        return self.data['id']
    
    @property
    def tag(self):
        return self.data['tag']
    
    @property
    def slug(self):
        return self.data['slug']
    
    def getAllGames(self) -> List[Dict]:
        return self.data['games']['data']
    
    def getRandomGame(self) -> TopGamesData:
        return TopGamesData(random.choice(self.getAllGames()))
    
    def getGameById(self, game_id: str) -> Union[TopGamesData, Dict]:
        for item in self.getAllGames():
            if item['id'] == game_id:
                return TopGamesData(item)
            
        return {}
    
class FuturedGamesObject(TopGamesObject):
    def __init__(self, jsresult: dict) -> None:
        super().__init__(jsresult)

    def getGameById(self, game_id: str):
        for item in self.getGames():
            if item['id'] == game_id:
                return FuturedGamesData(item)
            
        return {}
    
    def getGames(self) -> List[Dict]:
        return self.data
    
    def getRandomGame(self):
        return FuturedGamesData(random.choice(self.getGames()))

class FuturedGamesData(TopGamesData):
    def __init__(self, itemresult: dict) -> None:
        super().__init__(itemresult)

class NewGamesObject(TopGamesObject):
    def __init__(self, jsresult: dict) -> None:
        super().__init__(jsresult)

    def getGameById(self, game_id: str):
        for item in self.data:
            if item['id'] == game_id:
                return NewGamesData(item)
            
        return {}
    
    def getRandomGame(self):
        return NewGamesData(random.choice(self.data))

class NewGamesData(TopGamesData):
    def __init__(self, itemresult: dict) -> None:
        super().__init__(itemresult)

class ProcessedNewGamesObject(TopGamesObject):
    def __init__(self, jsresult: dict) -> None:
        super().__init__(jsresult)

    def getGames(self) -> List[Dict]:
        return self.data

    def getGameById(self, game_id: str):
        for item in self.getGames():
            if item['id'] == game_id:
                return ProcessedNewGamesData(item)
            
        return {}
    
    def getRandomGame(self):
        return ProcessedNewGamesData(random.choice(self.getGames()))

class ProcessedNewGamesData(TopGamesData):
    def __init__(self, itemresult: dict) -> None:
        super().__init__(itemresult)

class OriginalGamesObject(TopGamesObject):
    def __init__(self, jsresult: dict) -> None:
        super().__init__(jsresult)

    def getGameById(self, game_id: str):
        for item in self.getGames():
            if item['id'] == game_id:
                return OriginalGamesData(item)
            
        return {}
    
    def getRandomGame(self):
        return OriginalGamesData(random.choice(self.getGames()))

class OriginalGamesData(TopGamesData):
    def __init__(self, itemresult: dict) -> None:
        super().__init__(itemresult)

class SidebarTagsObject(object):
    def __init__(self, jsresult: dict) -> None:
        self.data = jsresult

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)
    
    def getRandomTag(self):
        return SidebarTagsData(random.choice(self.data))
    
    def getAllTags(self) -> List:
        return self.data

class SidebarTagsData(object):
    def __init__(self, itemresult: dict) -> None:
        self.data = itemresult

    def __str__(self) -> str:
        return json.dumps(self.data, indent=4)
    
    @property
    def name(self) -> str:
        return self.data['name']
    
    @property
    def slug(self) -> str:
        return self.data['slug']
    
    @property
    def en_slug(self) -> str:
        return self.data['enSlug']
    
    @property
    def title(self) -> str:
        return self.data['title']
    
    def getMenuWeight(self) -> int:
        return self.data['menuWeight']
    
    def isCategory(self) -> bool:
        return self.data['isCategory']

class CrazyGamesClient(object):
    def __init__(self) -> None:
        self.version = "1.0.0"
        self.heads = [
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 13_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/121.0.2277.107 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPX/2.2.0",
        "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.6261.62 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 Ddg/17.0",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 AtContent/95.5.5392.49",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 8.1.0; Mobile; rv:123.0) Gecko/123.0 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPX/2.2.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/116.0.1938.79 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 RDDocuments/8.4.8.940",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0.3 Mobile/15E148 Safari/604.1 RDDocuments/8.7.2.978",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 AtContent/95.5.5392.49",
        "Mozilla/5.0 (iPad; CPU OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Android 8.1.0; Mobile; rv:123.0) Gecko/123.0 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/116.0.1938.56 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 DuckDuckGo/7 Safari/605.1.15",
        "Mozilla/5.0 (Linux; Android 8.1.0; C5 2019 Build/OPM2.171019.012) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/122.0.6261.62 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 Config/91.2.2121.13",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.126 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Linux; Android 11; moto e20 Build/RONS31.267-94-14) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.64 Mobile Safari/537.36",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5; rv:123.0esr) Gecko/20100101 Firefox/123.0esr",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.86 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 OpenWave/94.4.4504.39",
        "Mozilla/5.0 (iPad; CPU OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/118.0.2088.68 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (iPad; CPU OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Herring/95.1.1930.31",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0 Unique/97.7.7286.70",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36 Trailer/93.3.3516.28",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 OpenWave/94.4.4504.39",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1 OPT/4.3.1",
        "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Mobile Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_2 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/120.0.2210.126 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0 OpenWave/94.4.4504.39",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_5; rv:123.0esr) Gecko/20100101 Firefox/123.0esr",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/117.0.2045.48 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 DuckDuckGo/7 Safari/605.1.15",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) EdgiOS/119.0.2151.105 Version/17.0 Mobile/15E148 Safari/604.1",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36 Edg/121.0.0.0",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:123.0) Gecko/20100101 Firefox/123.0];"
        ]

    def getSidebarTags(self) -> Union[SidebarTagsObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return SidebarTagsObject(json.loads(result.group(1))['props']['sidebarTags'])
        else:
            return {}

    def getTopGames(self) -> Union[TopGamesObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return TopGamesObject(json.loads(result.group(1))['props']['pageProps']['topGames']['data'])
        else:
            return {}
        
    def getHomePageGames(self) -> Union[HomePageGamesObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return HomePageGamesObject(json.loads(result.group(1))['props']['pageProps']['homepageCat'])
        else:
            return {}
        
    def getFeaturedGames(self) -> Union[FuturedGamesObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return FuturedGamesObject(json.loads(result.group(1))['props']['pageProps']['featuredGames']['data']['items'])
        else:
            return {}

    def getNewGames(self) -> Union[NewGamesObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return NewGamesObject(json.loads(result.group(1))['props']['pageProps']['newGames']['data']['items'])
        else:
            return {}
        
    def getProcessedNewGames(self) -> Union[ProcessedNewGamesObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return ProcessedNewGamesObject(json.loads(result.group(1))['props']['pageProps']['newGames']['data']['items'])
        else:
            return {}
        
    def getOriginalGames(self) -> Union[OriginalGamesObject, Dict]:
        resp = httpx.get("https://www.crazygames.com/", headers={
            "User-Agent": random.choice(self.heads)
        }).text
        parser = bs4.BeautifulSoup(resp, "html.parser")
        games = str(parser.findAll("script")[-1])
        pattern = re.compile(r'<script.*?>(.*?)</script>')
        result = re.search(pattern, games)
        if result:
            return OriginalGamesObject(json.loads(result.group(1))['props']['pageProps']['newGames']['data'])
        else:
            return {}

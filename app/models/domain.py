from datetime import datetime
from typing import List, Optional

class Football_Club:
    def __init__(
        self, 
        id: int, 
        name: str, 
        budget: int, 
        rating: int, 
        players: Optional[List[str]] = None,
        coach: Optional[str] = None,  
        creation_date: Optional[datetime] = None) -> None:
        
        self.id = id
        self.name = name
        self.budget = budget
        self.rating = rating 
        self.players = players if players is not None else []
        self.coach = coach if coach else "Unknow"
        self.creation_date = creation_date if creation_date else datetime.now()

class  Player:
    def __init__(self,
        id: int,
        name: str,
        rating: int, 
        creation_date: Optional[datetime] = None, 
        football_club: Optional[str] = None) -> None:
        if not (0<= rating <=5):
            raise ValueError("Рейтинг должен быть от 0 до 5.")
        
        self.id = id 
        self.name = name
        self.rating = rating 
        self.creation_date = creation_date if creation_date else datetime.now()

    
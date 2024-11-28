from datetime import datetime
from typing import List, Optional


class Football_Club:
    def __init__(
        self,  
        name: str, 
        budget: int,  
        players: Optional[List["Player"]] = None,
        coach: Optional["Trainer"] = None,  
        creation_date: Optional[datetime] = None) -> None:
        
        self.id = Sequence.getId()
        self.name = name
        self.budget = budget 
        self.players = players if players is not None else []
        self.coach = coach if coach else "Unknow"  
        self.creation_date = creation_date if creation_date else datetime.now()
    
    def remove_coach(self):
        if self.coach:
            print(f"Тренер {self.coach.name} удален из клуба {self.name}.")
        self.coach = None

    @property
    def rating(self) -> float:
        
        if not self.players: 
            players_average_rating = 0
        else:
            players_average_rating = sum(player["rating"] for player in self.players) / len(self.players)

        coach_rating = self.coach.rating if self.coach else 3

        return round(players_average_rating * (coach_rating/5), 1)




class  Player:
    def __init__(self,
        name: str,
        rating: int, 
        creation_date: Optional[datetime] = None, 
        football_club: Optional[Football_Club] = None) -> None:
        if not (0<= rating <=5):
            raise ValueError("Рейтинг должен быть от 0 до 5.")
        
        self.id = Sequence.getId() 
        self.name = name
        self.rating = rating 
        self.football_club = football_club
        self.creation_date = creation_date if creation_date else datetime.now()

class Trainer:
    def __init__(self, 
        name: str,
        rating: int,
        creation_date: Optional[datetime] = None,
        football_club: Optional[Football_Club] = None) -> None:
        if not (0<= rating <=5):
            raise ValueError("Рейтинг должен быть от 0 до 5.")

        self.id = Sequence.getId()
        self.name = name
        self.footbal_club = football_club
        self.rating = rating 
        self.creation_date = creation_date if creation_date is None else datetime.now()



class Sequence:
    _id: int = 0

    @classmethod
    def get_id(cls) -> int:
        cls._id += 1
        return cls._id
    


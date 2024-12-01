from datetime import datetime
from typing import List, Optional


class FootballClub:
    def __init__(
        self,  
        name: str, 
        budget: int,  
        coach: Optional["Trainer"] = None,  
        creation_date: Optional[datetime] = datetime.now(),
        players: Optional[List["Player"]] = [],
        ) -> None:
        
        self.id = Sequence.getId()
        self.name = name
        self.budget = budget 
        self.players = players 
        self.coach = coach
        self.creation_date = creation_date
    
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
        creation_date: Optional[datetime] = datetime.now(), 
        football_club: Optional[FootballClub] = None) -> None:
        
        self.id = Sequence.getId() 
        self.name = name
        self.rating = self._validation(rating) 
        self.football_club = football_club
        self.creation_date = creation_date 
    
    
    def _validation(self, rating: int) -> int:
        if not (0<= rating <= 5):
            raise ValueError("Рейтинг должен быть от 0 доп 5")
        return rating 
        

class Trainer:
    def __init__(self, 
        name: str,
        rating: int,
        creation_date: Optional[datetime] = datetime.now(),
        football_club: Optional[FootballClub] = None) -> None:

        self.id = Sequence.getId()
        self.name = name
        self.footbal_club = football_club
        self.rating = self._validation(rating) 
        self.creation_date = creation_date
    
    def _validation(self, rating: int) -> int:
        if not (0<= rating <= 5):
            raise ValueError("Рейтинг должен быть от 0 доп 5")
        return rating 

class Sequence:
    _id: int = 0

    @classmethod
    def get_id(cls) -> int:
        cls._id += 1
        return cls._id
    


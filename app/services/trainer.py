from app.models.domain import Trainer, FootballClub
from typing import List, Optional

trainers: List[Trainer] = []

def create_coach(name: str, rating: int, club: FootballClub) -> Trainer:
    coach = Trainer(name = name , rating = rating, football_club=club)
    trainers.append(coach)
    return coach

def delete_coach(coach_id: int, football_club: Optional[FootballClub] = None): 
    global trainers 
    coach_to_delete = next((coach for coach in trainers if coach.id == coach_id), None)

    if coach_to_delete:
        if football_club and football_club.coach == coach_to_delete:
            football_club.remove_coach()

        trainers.remove(coach_to_delete)
        print(f"Тренер {coach_to_delete.name} удален.")
        return True
    
    else: 
        print(f"Тренер с id {coach_id} не найден.")
        return False




def update(coach_id: int, name: str, rating: int, football_club: Optional[FootballClub] = None):
    global trainers
    coach_to_update = next((coach for coach in trainers if coach.id == coach_id), None)

    if coach_to_update: 
        coach_to_update.name = name
        coach_to_update.rating = rating

        if football_club: 
            coach_to_update.footbal_club = football_club
            print(f"Тренер с ID {coach_id} обновлен.")
    else: 
        print(f"Тренер с ID {coach_id} не найден.")

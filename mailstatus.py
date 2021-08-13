from requests import get
from typing import Any, Dict, List
from pydantic import BaseModel


class GameSession(BaseModel):
    turn: int
    phase: int
    players: List[str]
    last_played: str
    hours_left: int


def get_current_player(session: GameSession) -> str:
    return session.players[session.phase]


def get_sessions() -> List[GameSession]:
    ### Get all game sessions JSON via API
    response = get("https://www.freecivweb.org/mailstatus")
    sessions = []

    for session in response.json():
        sessions.append(GameSession.parse_obj(status_to_dict(session)))
    return sessions


def get_specific_session() -> GameSession:
    ### Remake this for other people to use
    ### this doesn't even do any validation
    session_list = get_sessions()
    for session in session_list:
        if "Sjal" and "Donmarcino" in session.players:
        ### just went with me and my friend here, this is to be reworked
            return session


def status_to_dict(session: List[Any]) -> Dict[str, GameSession]:
    ### Convert JSON list response to human-readable dict
    keys = ["turn", "phase", "players", "last_played", "hours_left"]
    return dict(zip(keys, session))

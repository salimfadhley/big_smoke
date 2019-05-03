import datetime
from dataclasses import dataclass, field
from typing import List

from bigsmoke.model.event import Event
from bigsmoke.model.location import Location


@dataclass
class Series:
    name: str
    location: Location
    about: str
    start_time: datetime.time = datetime.time(8, 0)
    price: str = "Free"
    events: List[Event] = field(default_factory=list)

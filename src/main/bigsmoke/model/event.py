import datetime
from dataclasses import field
from typing import List

from attr import dataclass

from bigsmoke.model.act import Act


@dataclass
class Event:
    date: datetime.date
    mc: Act
    acts: List[Act] = field(default_factory=list)

    def num_acts(self) -> int:
        return len(self.acts)

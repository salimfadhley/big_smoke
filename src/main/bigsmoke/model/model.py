from dataclasses import dataclass, field
from typing import List, Tuple

from bigsmoke.model.event import Event
from bigsmoke.model.series import Series


@dataclass
class SeriesAndEvent:
    series: Series
    event: Event

@dataclass
class Model:
    serieses: List[SeriesAndEvent] = field(default_factory=list)

    def all_events(self)->List[SeriesAndEvent]:
        events:List[SeriesAndEvent] = []
        for ss in self.serieses:
            for ee in ss.events:
                events.append(SeriesAndEvent(series=ss, event=ee))

        return sorted(events, key=lambda e: e.event.date)
import datetime
from typing import List

import bigsmoke.data.acts as a
from bigsmoke.model.act import Act
from bigsmoke.model.event import Event


def bs(date: datetime.date, acts: List[Act]) -> Event:
    return Event(date=date, acts=acts, mc=a.MARC_SALMON)


BIG_SMOKE_ALL_STARS_EVENTS = [
    bs(
        date=datetime.date(2019, 5, 13),
        acts=[
            a.NAZ_OSMANOGLU,
            a.JAY_BENNETT,
            a.SAMMY_HANNAH,
            a.COLIN_ROTHWELL,
            a.ALISHA_MAY.performing_as("Doris Kettle"),
            a.KATIE_HANDLEY,
            a.DAVE_THOMSON.performing_as("Sandiwch Board Guy"),
        ],
    )
]

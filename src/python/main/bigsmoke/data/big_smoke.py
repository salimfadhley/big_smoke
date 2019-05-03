import datetime
from typing import List

import bigsmoke.data.acts as a
from bigsmoke.model.act import Act
from bigsmoke.model.event import Event


def bs(date: datetime.date, acts: List[Act]) -> Event:
    return Event(date=date, acts=acts, mc=a.BROOKE_HOERR)


BIG_SMOKE_EVENTS = [
    bs(
        date=datetime.date(2019, 5, 2),
        acts=[
            a.JAMES_MEAKIN,
            a.CURRER_BALL,
            a.JENAN_YOUNIS,
            a.ROBBIE_FOX,
            a.ALISHA_MAY,
            a.LAURA_SMYTH,
            a.EMMANUEL_PAUL,
            a.MARCEL_HAGAN,
        ],
    ),
    bs(
        date=datetime.date(2019, 5, 9),
        acts=[
            a.NITYA_VARMA,
            a.ELLIOT_DALLAS,
            a.KIRSTY_HUDSON,
            a.NICK_EVERRITT,
            a.FATHIA_SARIPUSPITA,
            a.SHAWN_HOULT,
        ],
    ),
    bs(
        date=datetime.date(2019, 5, 16),
        acts=[
            a.SAMMY_HANNAH,
            a.MO_OMAR,
            a.JAKE_PICKFORD,
            a.MARIANA_FIEJO,
            a.KURREN_VARMA,
            a.ROSANNA_WOOD,
            a.MARA_MANKA,
            a.MARC_SALMON,
        ],
    ),
    bs(
        date=datetime.date(2019, 5, 23),
        acts=[a.LUKE_CHILTON, a.VASH_PERNIKAR, a.JAZ_MATTU, a.THOMAS_JAMES_ALLEN],
    ),
    bs(
        date=datetime.date(2019, 5, 30),
        acts=[a.MARTY_WILLIAMS, a.PETER_HOSE, a.ARCHIE_BRROKES_WATSON],
    ),
    bs(
        date=datetime.date(2019, 6, 6),
        acts=[a.BOB_MUNRO, a.DANIEL_MCKEON, a.RICARDO_MOTTI],
    ),
    bs(date=datetime.date(2019, 6, 13), acts=[a.DAVID_EAGLE, a.HARI_SRISKANTHA]),
    bs(date=datetime.date(2019, 6, 20), acts=[a.STEPHEN_CATLING]),
]

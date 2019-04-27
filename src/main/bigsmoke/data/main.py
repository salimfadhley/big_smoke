import datetime
from typing import List

from bigsmoke.data.big_smoke import BIG_SMOKE_EVENTS
from bigsmoke.data.big_smoke_all_stars import BIG_SMOKE_ALL_STARS_EVENTS
from bigsmoke.model.event import Event
from bigsmoke.model.location import Location
from bigsmoke.model.model import Model
from bigsmoke.model.series import Series

TODAY: datetime.date = datetime.date.today()


def filter_events(events: List[Event], the_date: datetime.date) -> List[Event]:
    return [e for e in events if e.date > the_date]


the_nell_of_old_drury = Location(
    name="Nell of Old Drury", address="29 Catherine Street, London WC2B 5JS"
)

big_smoke: Series = Series(
    name="Big Smoke",
    location=the_nell_of_old_drury,
    about="Our weekly stand-up and improvised comedy show.",
    events=filter_events(events=BIG_SMOKE_EVENTS, the_date=TODAY),
)


big_smoke_all_stars = Series(
    name="Big Smoke All Stars",
    location=the_nell_of_old_drury,
    about="The best acts from Big Smoke return to the stage once per month.",
    events=filter_events(events=BIG_SMOKE_ALL_STARS_EVENTS, the_date=TODAY),
)


def get_model() -> Model:
    return Model(serieses=[big_smoke, big_smoke_all_stars])

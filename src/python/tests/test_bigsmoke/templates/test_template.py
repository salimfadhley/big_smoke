import jinja2
from bigsmoke.templates import get_template


def test_template():
    t: jinja2.Template = get_template("listings.html")

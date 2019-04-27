import jinja2

from bigsmoke.data.main import get_model
from bigsmoke.model.model import Model
from bigsmoke.templates import get_template


def main(output_filename="listings.html"):
    template: jinja2.Template = get_template("listings.html")
    model:Model = get_model()
    with open(output_filename, "w") as output_file:
        output_file.write(template.render(m=model))

if __name__ == "__main__":
    main()
from pkg_resources import resource_stream, resource_string

import jinja2


def get_template(file_name: str) -> jinja2.Template:
    # this_module = __import__('bigsmoke.templates').templates
    template_str: str = resource_string("bigsmoke.templates", file_name).decode("UTF-8")
    return jinja2.Template(template_str)

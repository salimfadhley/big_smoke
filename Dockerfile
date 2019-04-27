FROM salimfadhley/testpython AS python
COPY . /project
RUN useradd python


FROM python AS bigsmokepython
RUN python -m pip install -r /project/src/requirements_dev.txt
RUN python -m pip install -e /project/src
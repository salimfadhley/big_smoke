

FROM salimfadhley/testpython AS python
RUN pip install --upgrade pip setuptools
COPY /src/python /src/python
RUN useradd python


FROM python AS bigsmokepython
WORKDIR /project/src
RUN python -m pip install -r /src/python/requirements_dev.txt
RUN pwd
RUN python -m pip install -e /src/python

FROM node AS base_vue
RUN npm install -g vue @vue/cli
USER 1000
FROM python:3.10-slim

WORKDIR /ContentMigrations


COPY . .

# add build-base for building packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    gcc \
    libc-dev \
    ;

# create and activate virtual environment
RUN python3 -m venv myenv
ENV PATH=/ContentMigrations/myenv/bin:$PATH

# # set environment variables
ENV TENANT=${TENANT}
ENV ACTION=${ACTION}
ENV TENANT=${URL}
ENV ACTION=${USERNAME}
ENV ACTION=${PASSWORD}
ENV ACTION=${APP}

# Install mstrio package
RUN pip install --no-cache-dir -r requirements.txt

# start the python script
CMD [ "python", "./ContentMigration.py" ]


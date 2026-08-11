# Build context is determined from `docker build -t <tag> <buildcontext_dir>`
# So, for example, your current working directory has requirements and backend.py do `docker build -t template-backend .` 
FROM python:3.12-slim AS base
LABEL authors="AUTHOR"
ENV PYTHONBUFFERED=1
# Bind mount requirements.txt to avoid copying
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --no-cache-dir --requirement /tmp/requirements.txt
# Need to give our temporary build container backend.py
EXPOSE 8000
WORKDIR /server
CMD ["python3", "src/backend.py"] 

# Docker COPY work exactly like cp, hence the ./src dest.
FROM base AS prod
COPY ./src ./src

# We could install dev requirements in here if needed.  
FROM base AS dev
VOLUME /server

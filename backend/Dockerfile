# Build context is determined from `docker build -t <tag> <buildcontext_dir>`
# So, for example, your current working directory has requirements and backend.py do `docker build -t template-backend .` 
FROM python:3.12-slim
LABEL authors="Daniel Morine"
ENV PYTHONBUFFERED=1
WORKDIR /server
# Bind mount requirements.txt to avoid copying
RUN --mount=type=bind,source=requirements.txt,target=/tmp/requirements.txt \
    pip install --requirement /tmp/requirements.txt
# Need to give our temporary build container backend.py
COPY backend.py . 
EXPOSE 8000
CMD ["python3", "backend.py"] 

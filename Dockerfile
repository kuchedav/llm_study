FROM python:3.8

RUN mkdir /app
WORKDIR /app/

COPY src/llm/. .

ENTRYPOINT ["tail", "-f", "/dev/null"]

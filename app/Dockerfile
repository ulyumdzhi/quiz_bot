FROM python:slim
ENV TOKEN=%YOUR_OWN_TELEGRAM_TOKEN_HERE%
COPY . .
RUN python loader.py
ENTRYPOINT [ "python", "main.py" ]
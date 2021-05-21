FROM python:3.9
WORKDIR /bot
COPY requirements.txt ./
RUN pip3 install -r requirements.txt
COPY bot bot
COPY tokens tokens
ENV PYTHONPATH=/bot
EXPOSE 8000
CMD python3 bot/main.py
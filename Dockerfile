FROM Python

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY /datasets .

COPY /src .

COPY main.py .

VOLUME /app-password

EXPOSE 80

CMD ["mkdir","models"]

ENTRYPOINT ["python3","main.py"]
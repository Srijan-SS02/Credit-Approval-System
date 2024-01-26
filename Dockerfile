FROM python:3.11-slim
WORKDIR /app
COPY requirements.txt .
RUN 
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
RUN chmod +x entrypoint.sh
CMD ["sh","./entrypoint.sh"]
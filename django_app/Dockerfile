FROM python:3.12-slim
WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Run migrations and start the server
CMD sh -c "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"
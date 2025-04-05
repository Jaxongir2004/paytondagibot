# Python bazaviy rasm
FROM python:3.10-slim

# Ishchi papkani belgila
WORKDIR /app

# Talablarni o‘rnatish
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Kodni nusxalash
COPY . .

# Webhook uchun portni belgilash
ENV PORT 8080

# Flaskni ishga tushirish
CMD ["python", "bot.py"]

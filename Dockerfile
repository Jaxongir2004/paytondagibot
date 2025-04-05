# Asosiy Python image'ni ishlating
FROM python:3.9-slim

# Loyihani papkaga ko‘chirish
WORKDIR /app

# Kutubxonalarni o‘rnatish
COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Bot fayllarini qo‘shish
COPY . .

# Botni ishga tushirish
CMD ["python", "bot.py"]

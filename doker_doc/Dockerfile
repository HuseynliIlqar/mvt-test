FROM python:3.10-slim

# Virtuallı mühitdə Python bytecode fayllarını yazmamaq və stdout'u buffer etməmək
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# İş qovluğu
WORKDIR /app

# Paket asılılıqlarını qopyala və quraşdir
COPY requirements.txt ./
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Layihə fayllarını konteynerə kopyala
COPY . .

# Portu elan et
EXPOSE 8000

# Django serverini gunicorn vasitəsilə 0.0.0.0:8000 portunda işə sal
CMD ["gunicorn", "mvt_test.wsgi:application", "--bind", "0.0.0.0:8000"]

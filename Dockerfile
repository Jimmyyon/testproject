FROM python:3.9.5

WORKDIR /app

COPY . .

RUN apt-get update && apt-get install -y wget gnupg ca-certificates fonts-liberation \
    libatk-bridge2.0-0 libatk1.0-0 libcups2 libdrm2 libxkbcommon0 libnss3 libxcomposite1 \
    libxdamage1 libxrandr2 libgbm1 libasound2 libpangocairo-1.0-0 libxshmfence1 libgtk-3-0 \
    libx11-xcb1 libxss1 libxtst6 && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip \
    && pip install -r requirements.txt \
    && python -m playwright install

CMD ["pytest"]
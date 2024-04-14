FROM python:3.12.2

# Instalo o con
RUN apt-get update && apt-get install -y cron

WORKDIR /app
#copio pro diretorio do docker
COPY . /app

RUN pip install -r requirements.txt

# Adiciona o cronjob para executar minha main.py a cada 5 minutos 
RUN echo "*/5 * * * * root python /app/main.py" > /etc/cron.d/execute_script

# aqui habilito o cron
RUN crontab /etc/cron.d/execute_script

# Inicia o cron em segundo plano
CMD ["cron", "-f"]



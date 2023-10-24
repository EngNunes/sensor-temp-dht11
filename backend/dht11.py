import Adafruit_DHT
import time
import sqlite3
import datetime
import logging
import pytz

#configuração do sensor dht11
DHT_SENSOR = Adafruit_DHT.DHT11
DHT_PIN = 14

#configurando a Timezone
tz = pytz.timezone('America/Sao_Paulo')

#numero de amostras
num_samples = 100

logging.basicConfig(filename='log_sensor_quarto.log', level=logging.DEBUG)
try:
    #intervalo entre as amostras em segundos 30min -> (60s/1min)
    # sample_interval = 30 * 60 
    # sample_interval =  60 # 1 em 1 minuto teste
    sample_interval =  120 # 2min

    #criando o banco de dados
    connection = sqlite3.connect('/home/pi/temperature-sensor/data/sensor_quarto.db')
    # connection = sqlite3.connect('../data/sensor_quarto.db')
    # connection = sqlite3.connect('sensor_quarto.db')
    cursor = connection.cursor()
    cursor.execute(
        '''
        CREATE TABLE IF NOT EXISTS sensor_data_quarto (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        hora TIME,
        temperatura REAL,
        umidade REAL
        )    
    '''
    )
    connection.commit()

    #loop para coleta
    for i in range(num_samples):
        #leitura sensor
        humidity, temperature = Adafruit_DHT.read(DHT_SENSOR, DHT_PIN)
        #obtencao de data e hora atual
        current_time = datetime.datetime.now(tz)
        current_date = current_time.strftime("%d-%m-%Y")
        current_time = current_time.strftime("%H:%M:%S")

        #inserção de dados no banco
        cursor.execute("INSERT INTO sensor_data_quarto (data,hora,temperatura,umidade) VALUES (?,?,?,?)", (current_date, current_time, temperature, humidity))
        connection.commit()
        time.sleep(sample_interval)
        # print(f'Coleta de {num_samples} concluída')
    connection.close()
    logging.info('Leitura realizada com sucesso')
except Exception as e:
    logging.error(f'Erro de Execução:{str(e)}',exc_info=True)

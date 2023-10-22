from flask import Flask, render_template
import sqlite3

app = Flask(__name__)

@app.route('/')

def home():
    return "<H2>Sensor webpage running...<H2>"

@app.route('/dados')

def mostrar_dados():
    # connection = sqlite3.connect('../sensor_quarto.db')
    connection = sqlite3.connect('../data/sensor_quarto.db')
    cursor = connection.cursor()
    cursor.execute("SELECT data, hora, temperatura, umidade FROM sensor_data_quarto")
    dados = cursor.fetchall()
    connection.close()

    return render_template('index.html', dados=dados)
# def run():
#     app.run(host='0.0.0.0', port=5000)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
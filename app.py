from flask import Flask, render_template
from data import logs  # importa a lista compartilhada

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', logs=logs)

if __name__ == '__main__':
    import mqtt_client  # inicia o cliente MQTT que vai manipular logs
    app.run(debug=True)

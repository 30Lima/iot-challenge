import paho.mqtt.client as mqtt
from data import logs
from datetime import datetime

# Callback quando o cliente se conecta ao broker
def on_connect(client, userdata, flags, rc):
    print("Conectado com código de resultado: " + str(rc))
    client.subscribe("heimdall/entrada")  

# Callback quando uma mensagem é recebida
def on_message(client, userdata, msg):
    try:
        payload = msg.payload.decode()
        print(f"Mensagem recebida: {payload}")

        placa, zona = payload.split(',')

        log = {
            "hora": datetime.now().strftime("%H:%M:%S"),
            "placa": placa,
            "zona": zona
        }

        logs.append(log)
        print(f"Log adicionado: {log}")
    except Exception as e:
        print(f"Erro ao processar mensagem: {e}")

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("broker.hivemq.com", 1883, 60)

client.loop_start()

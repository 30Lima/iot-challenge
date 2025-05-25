import time, random
import paho.mqtt.publish as publish

placas = ["ABC1234", "XYZ5678", "MNO4567", "DEF0001"]
zonas = ["Combustão", "Elétrica", "Zona Combustão 2"]

while True:
    placa = random.choice(placas)
    zona = random.choice(zonas)
    mensagem = f"{placa},{zona}"
    publish.single("heimdall/entrada", mensagem, hostname="broker.hivemq.com")
    print(f"Enviado: {mensagem}")
    time.sleep(5)  # enviando logs a cada cinco segundos para o 'dashboard'

# HEIMDALL - Localização e Monitoramento de Motos no Pátio
> Solução para o challenge da Mottu promovido pela FIAP

## Integrantes

| Nome Completo               | RM       |
|-----------------------------|----------|
| Pedro Henrique Lima Santos  | 558243   |
| Vitor Gomes Martins         | 558244   |
| Leonardo Pimentel Santos    | 557541   |

## Descrição da Solução

O **HEIMDALL** é uma solução integrada composta por um aplicativo mobile (React Native) e um sistema de simulação com IoT e dashboard web (Python + Flask + MQTT). Seu objetivo é facilitar o processo de **localização e monitoramento de motocicletas dentro do pátio logístico da Mottu**, organizando as motos por zonas e exibindo logs de entrada em tempo real.

### Funcionalidades

- **Aplicativo mobile** com navegação via Drawer, telas de Splash, Login, Cadastro, Home, Perfil e Sobre.
- Armazenamento local do nome de usuário com `AsyncStorage`.
- Interface desenvolvida com foco em acessibilidade, responsividade e boas práticas de UX.
- **Dashboard web** que exibe em tempo real os logs das entradas das motos no pátio com nome da zona, placa e horário.
- Integração MQTT para simular envio automático de dados de sensores IoT.

---

## Estrutura do Projeto

```bash
iot-challenge/
│
├── __pycache__/          # Arquivos compilados do Python
├── app.py                # Servidor Flask que renderiza o dashboard
├── data.py               # Lista compartilhada entre Flask e MQTT
├── mqtt_client.py        # Cliente MQTT que recebe dados e atualiza os logs
├── simulador.py          # Script que simula entradas via MQTT
│
├── iot/                  # Protótipos e circuitos Tinkercad
│
├── static/               # Arquivos CSS e estáticos
│   └── style.css         # Estilo do dashboard HTML
│
└── templates/
    └── index.html        # Template HTML Jinja para o dashboard
```

---

## Tecnologias Utilizadas

- Python 3
- Flask
- MQTT (Paho MQTT)
- HTML + CSS
- React Native + Expo (para a interface mobile)
- Tinkercad (para simulação de sensores IoT)
- GitHub (versionamento e repositório)

---

## Instruções de Uso

### Pré-requisitos

- Python 3 instalado
- pip instalado
- Git instalado

### Instalação

1. **Clone o repositório:**

```bash
git clone https://github.com/30Lima/iot-challenge.git
```

2. **Acesse o diretório do projeto:**

```bash
cd iot-challenge
```

3. **Instale as dependências:**

```bash
pip install flask
pip install paho-mqtt
```

4. **Execute o servidor:**

```bash
python app.py
```

O servidor Flask será iniciado em `http://localhost:5000`. A cada 5 segundos o dashboard se atualiza automaticamente para exibir as últimas entradas simuladas via MQTT.

---

## Resultados Parciais

- Interface mobile funcional desenvolvida em React Native.
- Dashboard funcional em Flask recebendo dados MQTT em tempo real.
- Simulação de entrada de motos via script Python.
- Protótipos de circuitos representando sensores de entrada feitos no Tinkercad.

---

## Links de Circuitos e Protótipos

- **Circuito de entrada IoT (Tinkercad):**
```bash
https://www.tinkercad.com/things/6VgHfOcavEk-iot-challenge
```

- **Representação simplificada da vaga:**
```bash
https://www.tinkercad.com/things/dk7eaNavA3N-esbocoexplicacao
```

- **Vídeo Pitch(Iot) da solução:**
```bash
https://youtu.be/v5KxRu1UJf4
```

- **Vídeo Pitch(solução) da solução:**
- > Este é o pitch que foi realizado para a explicação **completa** da solução. A sua visualização é opcional, mas é de importância para entender melhor como funciona o Heimdall.
```bash
https://youtu.be/VWbErLEcsRs
```

---

## Observações

Este projeto foi desenvolvido como parte do challenge proposto pela FIAP em parceria com a Mottu, com foco em arquitetura IoT, mobile e integração de sistemas com uso de tecnologias emergentes e simulações de campo.

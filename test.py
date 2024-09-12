import paho.mqtt.client as mqtt
import json
import subprocess
import platform
import sys

# MQTT服務器的IP地址
# mqtt_server = "35.185.143.79"
mqtt_server = "140.112.45.233"
# mqtt_server = "localhost"
# MQTT主題
# topic = "65534/report"
pubTopic = "6/report"

subTopic = "testpm2"

# 當連接到MQTT服務器時調用


def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    print('hello')
    # 訂閱主題
    client.subscribe(subTopic)

# 當接收到從MQTT服務器發布的消息時調用


def on_message(client, userdata, msg):
    # 把byte轉為string
    payload = str(msg.payload, encoding = 'utf-8')
    status = ""
    print(f"Received message: {msg.topic} {payload}")
    if payload == "checkUpdated":
        # 這裡實作關閉該程式
        command = "git rev-parse HEAD"
        Cid = subprocess.run(command, capture_output=True, universal_newlines=True, shell=True).stdout
        command = "git pull"
        execute = subprocess.run(command, capture_output=True, universal_newlines=True, shell=True)
        err = execute.stderr
        command = "git rev-parse HEAD"
        _Cid = subprocess.run(command, capture_output=True, universal_newlines=True, shell=True).stdout
        if Cid != _Cid:
            status = "success"
            sys.exit(0)
        else:
            if err:
                status = "error"
                print(err)
            else:
                status = "retain"
        print(status)

    

# 創建MQTT客戶端實例
client = mqtt.Client()

# 指定連接和消息接收的回調函數
client.on_connect = on_connect
client.on_message = on_message

# 連接到MQTT服務器
client.connect(mqtt_server, 1883, 60)

# 開始循環處理網絡事件，包括與MQTT服務器的連接和消息的接收
client.loop_forever()

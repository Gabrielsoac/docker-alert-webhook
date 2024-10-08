import docker as dkr
import datetime as dt
import requests as rq 

##client = dkr.from_env() -> busca pelas variáveis de ambiente

client = dkr.DockerClient(base_url='unix://var/run/docker.sock')
#webhook_discord_url = input("Enter the webhook_url: ")
webhook_discord_url = input('Enter the webhook URL: ')

for event in client.events(decode=True):
    #if(event['Action'] == 'die'):

    if(event['Type'] == 'network'):
        continue

    container_id = event["id"]
    container_action = event["Action"]
    container_name = event["Actor"]["Attributes"]["name"]
    container_epoch_time = event["time"]
    container_time_stamp = dt.datetime.fromtimestamp(container_epoch_time)
    
    payload = {"content": f"Alert \n Container ID: {container_id}\n Container Name: {container_name}\n Action:{container_action} \nTime: {container_time_stamp}"}
    rq.post(webhook_discord_url, data=payload)
    
client.close()




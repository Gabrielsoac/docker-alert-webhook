import docker as dkr
import datetime as dt

##client = dkr.from_env() -> busca pelas variáveis de ambiente

client = dkr.DockerClient(base_url='unix://var/run/docker.sock')

for event in client.events(decode=True, filters={'event':'die'}):
    #if(event['Action'] == 'die'):
        #print(event)

    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    container_epoch_time = event["time"]
    container_time_stamp = dt.datetime.fromtimestamp(container_epoch_time)
    print(f"Alert \n Container ID: {container_id}\n Container Name: {container_name}\n Time: {container_time_stamp}")

client.close()




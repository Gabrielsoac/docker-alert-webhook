import docker as dkr

##client = dkr.from_env() -> busca pelas variáveis de ambiente

client = dkr.DockerClient(base_url='unix://var/run/docker.sock')

for event in client.events(decode=True, filters={'event':'die'}):
    #if(event['Action'] == 'die'):
        #print(event)

    container_id = event["id"]
    container_name = event["Actor"]["Attributes"]["name"]
    container_epoch_time = event["time"]
    
    print(f"Alert \n Container ID: {container_id}\n Container Name: {container_name}\n Time: {container_epoch_time}")

client.close()




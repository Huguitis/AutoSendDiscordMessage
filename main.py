from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
import json
#Load Config
with open('./config.json') as f:
  data = json.load(f)
  for c in data['Config']:
        print('Loading...')
channelid = c['channelid'] #modify this in config.json
token = c['token'] #modify this in config.json
message = c['message'] #modify this in config.json
header_data = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": token
} 
 
def get_connection(): 
	return HTTPSConnection("discordapp.com", 443) 
 
def send_message(conn, channel_id, message_data): 
    try: 
        conn.request("POST", f"/api/v7/channels/{channel_id}/messages", message_data, header_data) 
        resp = conn.getresponse() 
         
        if 199 < resp.status < 300: 
            print("Message Sent") 
            pass 
 
        else: 
            stderr.write(f"HTTP {resp.status}: {resp.reason}\n") 
            pass 
 
    except: 
        stderr.write("Error\n") 
 
def main(): 
	message_data = { 
		"content": message, 
		"tts": "false"
	} 
 
	send_message(get_connection(), channelid, dumps(message_data)) 
 
if __name__ == '__main__': 
	while True:    
		main()      
		sleep(3600) #How often the message will be sent (in seconds), every 1 hour = 3600

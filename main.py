from http.client import HTTPSConnection 
from sys import stderr 
from json import dumps 
from time import sleep 
 
header_data = { 
	"content-type": "application/json", 
	"user-agent": "discordapp.com", 
	"authorization": "ACCOUNT TOKEN"
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
		"content": "Hey, I will send this message every 1 hour.", 
		"tts": "false"
	} 
 
	send_message(get_connection(), "CHANNEL ID", dumps(message_data)) 
 
if __name__ == '__main__': 
	while True:    
		main()      
		sleep(3600) #every 1 hour = 3600

import time
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from gpiozero import Button, Buzzer
from time import sleep
from signal import pause

buzzer = Buzzer(17)   # Define active buzzer PIN out
garage_door = Button(4)  # Define button PIN out
start = time.time()

period_of_time = 43200 # Time to run the monitoring in seconds

while (time.time() < start + period_of_time):
       
    if garage_door.is_pressed:
        url = 'https://www.pushsafer.com/api' # Destination URL
        post_fields = {                       # Set POST fields here
        "t" : 'Garage Open',                  # Alert title
        "m" : 'Check%20the%20garage%20door!', # Alert message
        "v" : 1,                              # Vibrate yes:no
        "d" : 39292,                          # Device ID
        "k" : '?'                             # Private key, you need a pushsafer account
        }

        request = Request(url, urlencode(post_fields).encode())
        json = urlopen(request).read().decode()
        print(json)
        print("The door is open!")
        buzzer.on()
        sleep(3)
        buzzer.off()
        # sleep(2)
    else:
        print("The door is closed!")
    sleep(600) # How long before we check again in seconds
    
  





# door_open_alert
A script to alert you if a door is open, within a certain time window.

With the use of a RaspberryPI, ths kit https://www.amazon.co.uk/gp/product/B00DBDT6TY/ref=ppx_yo_dt_b_asin_title_o02_s00?ie=UTF8&psc=1 and this script, you can send a push message and sound a buzzer (if you have one) if a door is open after a certain time of day. (You need a Pushsafer account, which has a cost)

Note you need to run the script via Cron 0 19 * * * /the_script.py to set your start time and use the Python script to define when it breaks (12 hours later in current version)

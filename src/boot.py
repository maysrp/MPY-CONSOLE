from machine import Pin,freq
from config import config
import shell as sh 
ok=Pin(8,Pin.IN,Pin.PULL_UP)
freq(240000000)
def shell():
    con.cls()
    sh.shell()
    
if ok.value():
    import start
    start.scr.bgcolor=0
    con=config(start)
    con.windows()





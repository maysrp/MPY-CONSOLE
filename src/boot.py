from machine import Pin,freq
from config import config
import shell as sh 
ok=Pin(8,Pin.IN,Pin.PULL_UP)
freq(240000000)
def shell():
    con.small()
    con.cls()
    sh.shell()
    

bl=Pin(16,Pin.OUT)
def light(t):
    if bl.value():
        bl.value(0)
    else:
        bl.value(1)
    
if ok.value():
    ok.irq(trigger=Pin.IRQ_RISING, handler=light)
    import start
    con=config(start)

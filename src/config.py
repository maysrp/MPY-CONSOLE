import st7789
from machine import SoftI2C,Pin,UART,Timer,SPI
import time
import network
import urequests



class config(object):
    def __init__(self,start):
        self.start=start
        self.WLAN=network.WLAN()
        self.WLAN.active(True)
        self.tft=st7789.ST7789(
            SPI(2, baudrate=40000000, sck=Pin(41), mosi=Pin(38)),
            240,
            320,
            cs=Pin(39, Pin.OUT),
            dc=Pin(40, Pin.OUT),
            backlight=Pin(36, Pin.OUT),
            reset=Pin(42, Pin.OUT),
            rotation=3,
            color_order=st7789.RGB,
            inversion=False)
    def jpg(self,jpg):
        self.tft.init()      
        self.tft.jpg(jpg,0,0)
    def bg(self,bgx):
        self.start.scr.bg=bgx
        self.start.scr.cls()
    def bgcolor(self,color):
        self.start.scr.bgcolor=color
    def fgcolor(self,color):
        self.start.scr.fgcolor=color
    def windows(self):
        self.bg("windows.jpg")
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(986)
    def ubuntu(self):
        self.bg("ubuntu.jpg")
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(st7789.color565(123,10,40))
    def pao(self):
        self.bg("pao.jpg")
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(st7789.color565(32,86,174))
    def default(self):
        self.bg(False)
        self.fgcolor(st7789.color565(242, 242, 242))
        self.bgcolor(st7789.color565(0,0,0))
        self.start.scr.cls()
    def green(self):
        self.bg(False)
        self.bgcolor(st7789.color565(0,0,0))
        self.fgcolor(st7789.color565(166, 227, 45))
        self.start.scr.cls()
    def wifi(self,name,password):
        self.WLAN.connect(name,password)
    def ifconfig(self):
        return self.WLAN.ifconfig()
    def get(self,url):
        return urequests.get(url)
    def cls(self):
        self.start.scr.cls()

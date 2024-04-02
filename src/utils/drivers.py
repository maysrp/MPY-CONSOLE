#ST7789
from machine import Pin, SPI, freq
import st7789

class SCREEN():
    def __init__(self, width, height):
        self.tft=st7789.ST7789(
        SPI(2, baudrate=40000000, sck=Pin(41), mosi=Pin(38)),
        height,
        width,
        cs=Pin(39, Pin.OUT),
        dc=Pin(40, Pin.OUT),
        backlight=Pin(36, Pin.OUT),
        reset=Pin(42, Pin.OUT),
        rotation=3,
        color_order=st7789.RGB,
        inversion=False)
        self.width = width
        self.height = height
        self.tft.init()
        self.tft.fill(0)

#BC6561 KEYBOARD
from machine import UART,Pin
import time

key_map={
0:b'q',1:b'w',7:b'e',14:b'r',16:b't',23:b'y',21:b'u',30:b'i',28:b'o',10:b'p',
3:b'a',8:b's',9:b'd',20:b'f',15:b'g',22:b'h',27:b'j',34:b'k',29:b'l',31:b'\x08',
4:None,12:b'z',11:b'x',19:b'c',18:b'v',25:b'b',26:b'n',33:b'm',32:None,24:b'\r\n',
13:b"exec(open('run.py').read())\r\n",6:b'=',5:b' ',2:b'\t',17:None,
    }
key_map_upper={
0:b'Q',1:b'W',7:b'E',14:b'R',16:b'T',23:b'Y',21:b'U',30:b'I',28:b'O',10:b'P',
3:b'A',8:b'S',9:b'D',20:b'F',15:b'G',22:b'H',27:b'J',34:b'K',29:b'L',31:b'\x08',
4:None,12:b'Z',11:b'X',19:b'C',18:b'V',25:b'B',26:b'N',33:b'M',32:None,24:b'\r\n',
13:b"\t",6:b'0',5:b' ',2:b'\x04',17:None,
    }

key_map_sym={
0:b'#',1:b'1',7:b'2',14:b'3',16:b'(',23:b')',21:b'_',30:b'-',28:b'+',10:b'@',
3:b'*',8:b'4',9:b'5',20:b'6',15:b'/',22:b':',27:b';',34:b"'",29:b'"',31:b'\x08',
4:None,12:b'7',11:b'8',19:b'9',18:b'?',25:b'!',26:b',',33:b'.',32:None,24:b'\r\n',
13:b"\t",6:b'0',5:b' ',2:b'import',17:None,
    }
key_map_sym_add={
0:b'#',1:b'1',7:b'2',14:b'3',16:b'[',23:b']',21:b'_',30:b'-',28:b'+',10:b'@',
3:b'*',8:b'4',9:b'5',20:b'6',15:b'/',22:b':',27:b';',34:b"'",29:b'"',31:b'\x08',
4:None,12:b'7',11:b'8',19:b'9',18:b'?',25:b'!',26:b',',33:b'.',32:None,24:b'\r\n',
13:b"\t",6:b'0',5:b' ',2:b'import',17:None,
    }
class KEYBOARD():
    def __init__(self):
        self.uart=UART(1,9600,rx=15,tx=3)
        self.alt=False
        self.upper=False
        self.bl=Pin(16,Pin.OUT)
        self.bl_state=False
        self.sym_add=False

    def check_key(self):
        rx_data=self.uart.read()
        if rx_data!=None:
            key_num=rx_data[0]
            if key_num==4:
                self.alt=True
            elif key_num==132:
                self.alt=False
                self.upper=False
            elif key_num==17 and not self.upper:
                 self.upper=True
                 self.bl.on()
            elif key_num==17 and self.upper:
                self.upper=False
                self.bl.off()
            elif key_num==32 and not self.sym_add:
                 self.sym_add=True
            elif key_num==32 and self.sym_add:
                self.sym_add=False
            if key_num>127:
                return None
            if self.alt:
                return key_map_sym[key_num]
            elif self.upper:
                return key_map_upper[key_num]
            elif self.sym_add:
                return key_map_sym_add[key_num]
            else:
                return key_map[key_num]
            

            
    





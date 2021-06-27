import snap7
from snap7.util import *
from snap7.snap7types import *
from threading import Timer

data = []
plc = snap7.client.Client()

plc.connect('192.168.10.10', 0, 1)

def get_n_title():
    plc_a = plc.read_area(0x84, 1, 0, 2)                # 长度为2读取的最小值为一个byte

    plc_aa = get_int(plc_a, 0)                          # DB1.DBW0.0

    plc_b = plc.read_area(0x84, 1, 2, 4)                

    plc_bb=get_dword(plc_b, 0)                          # DB1.DBD2.0

    plc_c = plc.read_area(0x84, 1, 6, 4)                

    plc_cc = get_real(plc_c, 0)                         # DB1.DBD6.0

    print(plc_aa, plc_bb, plc_cc)                       # 打印数值
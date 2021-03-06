#!/usr/bin/env python3
# coding=utf-8

import time as T
import socket as sk
import threading as th

C = sk.socket(sk.AF_INET, sk.SOCK_DGRAM)

try:
    while True:
        b = input('enter : ')
        if b == 'quit':
            break
        print('sendto :', b)
        b = b.encode('utf-8')
        C.sendto(b, ('0.0.0.0', 6789))
        C.settimeout(15)
        data, address = C.recvfrom(64)
        data = data.decode('utf-8')
        print('recvfrom :', data)

except:
    print('有接收异常。')
    raise
finally:
    C.close()

print('Client exit.')

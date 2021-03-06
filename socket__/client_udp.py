#!/usr/bin/env python3
# coding=utf-8
import socket
import time
import sys

buf = 1024

serverip = sys.argv[1]

try:

    udp_C = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
except:
    print('有初始化异常。')
    raise


try:
    while 1:
        input0 = input('enter: ')
        data = input0.encode('utf-8')
        udp_C.sendto(data, (serverip, 6789))
        if input0 == 'quit':
            break
        data, address = udp_C.recvfrom(1024)

        data = data.decode('utf-8')
        print(data)
except:
    print('有发送异常。')
    raise

finally:
    udp_C.close()

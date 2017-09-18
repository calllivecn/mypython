#!/usr/bin/env python3
#coding=utf-8

from threading import Thread
from subprocess import Popen,PIPE
import signal,os


ENV={"MEM_MIN":'',"MEM_MAX":'',"MC_SERVER":''}

for key in ENV.keys():
	ENV[key] = os.getenv(key)

CMD='java -Xms{MEM_MIN}M -Xmx{MEM_MAX}M '\
	'-jar {MC_SERVER}'.format(**ENV)

sub_exit_cmd='stop'

p = Popen(CMD,stdin=PIPE,shell=True)

def out():
	while True:
		data = p.stdout.readline()
		print(data)


def input_():
	cmd = ''
	while cmd != sub_exit_cmd:
		cmd = input()
		cmd2 = cmd + '\n'
		p.stdin.write(cmd2.encode())
		p.stdin.flush()

ppid = os.getpid()

print('father pid',ppid)
print('sub pid ',p.pid)

def sig_handler(sig_number,SIG):
	cmd = sub_exit_cmd + '\n'
	p.stdin.write(cmd.encode())
	p.stdin.flush()

signal.signal(signal.SIGTERM,sig_handler)



th = Thread(target=input_,daemon=True)
th.start()

print('wait sub end...')

try:
	print('subprocess returncode:',p.wait())
except KeyboardInterrupt:
	sig_handler(1,2)

print('exit...')


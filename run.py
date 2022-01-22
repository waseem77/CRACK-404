#coding=utf-8
#!/usr/bin/python2
import os
import random
import sys
os.system('rm -rf .txt')
for n in range(5999):
    nmbr = random.randint(1111111, 9999999)
    sys.stdout = open('.txt', 'a')
    print nmbr
    sys.stdout.flush()

reload(sys)
sys.setdefaultencoding('utf8')
from rdx import main_menu
main_menu()

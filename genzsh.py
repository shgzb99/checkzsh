import platform
from ctypes import *

# if platform.system() == 'Windows':
#     libc = cdll.LoadLibrary('msvcrt.dll')
# elif platform.system() == 'Linux':
#     libc = cdll.LoadLibrary('libc.so.6')
#
# libc.printf(b'Hello ctypes!\n')


# dll = cdll.LoadLibrary(r'C:\Users\Administrator\Documents\PycharmProjects\python36\checkzsh\ZiKaoZS.dll')
dll = windll.LoadLibrary(r'C:\Users\Administrator\Documents\PycharmProjects\python36\checkzsh\ZiKaoZS.dll')

dll.GetZshJym.restype = c_char
jym = dll.GetZshJym(b'6531341502114090')#65313415021140905

print(jym)

with open('zsh.txt','r',encoding='gbk') as f:
    zshs = f.readlines()

for zsh in zshs:
    jym = dll.GetZshJym(zsh[0:14].encode('utf-8'))
    jym = jym.decode()
    if (jym != zsh[15]) and (zsh[9:11] in['17','18','19']) :
        print('{} {}'.format(zsh[0:16],jym))
        # print('{} {}'.format(zsh[15],jym))

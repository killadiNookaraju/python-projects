import pywhatkit

wno = input('whatapp no :')
msg = input("msg: ")
hr = int(input('hour(24 hours format): '))
mnt = int(input('minutes; '))
pywhatkit.sendwhatmsg('+91'+ wno,msg,hr, mnt)
import datetime 
import pyperclip

now = datetime.datetime.now()
currenttimestamp = str(now.year) + str(now.month) + str(now.day) + '-' + str(now.hour) + str(now.minute) + '-' + str(now.second)
#print (now.year,now.month,now.day,'-',now.hour,now.minute,'-',now.second,sep='')
#print (currenttimestamp)
localtimestamp = now.strftime("%Y%m%d-%H%M-%S")

print(localtimestamp)

pyperclip.copy(localtimestamp)
spam = pyperclip.paste()
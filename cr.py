import datetime 
import pyperclip

now = datetime.datetime.now()
currenttimestamp = str(now.year) + str(now.month) + str(now.day) + '-' + str(now.hour) + str(now.minute) + '-' + str(now.second)
#print (now.year,now.month,now.day,'-',now.hour,now.minute,'-',now.second,sep='')
print (currenttimestamp)


pyperclip.copy(currenttimestamp)
spam = pyperclip.paste()
import os
os.system("cat /proc/net/dev | grep wlo1  >> wlo1Log")
strings =os.popen("cat /proc/net/dev | grep wlo1").read()
strings = strings.split(" ")[3]
mb =int(strings)/(1024*1024)
print("Data used is {:.2f} MB".format(mb))

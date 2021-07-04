#Banner
print("\033[1;32;40m  _  _    ___  _  _")
print("\033[1;36;40m | || |  / _ \| || |")
print("\033[1;33;40m | || |_| | | | || |_")
print("\033[1;35;40m |__   _| |_| |__   _|")
print("\033[1;34;40m    |_|  \___/   |_|")
print("\n\n\033[1;30;40m Made By Benjamin-X")
#File name
fname = str(input("\033[1;36;40mEnter file name:"))
#start with
rfrom = int(input("\n\033[1;33;40mFrom:"))
#End at
rend = int(input("\n\n\033[1;32;40mEnd:"))
print("\n\n\033[1;33;40mCreating....\n\n")
for i in range (rfrom,rend):
   b = str(i)
   print("\033[1;32;40m" + b)
   file = open(fname,'a')
   file.write("\n"+b)
print("\n Done....!")
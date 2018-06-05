import datetime
import sys
import time

#print(datetime.datetime.now())

for x in range(100):
	time.sleep(0.5) # Un dalay de medio segundo. Nos permite visualizar como se imprime nuestro texto....
	#sys.stdout.write("Texto")
	sys.stdout.write("\r%d %%" % x)
	sys.stdout.flush() #Para que se vea de nuevo..
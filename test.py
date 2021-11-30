import os
import time

start_time = time.time()
f = open("Boudin-Torres-2006.txt", "r")
for i in range(0,10000):
    str1 = f.read()


print("--- %s seconds ---" % (time.time() - start_time))

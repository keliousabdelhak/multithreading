from threading import Thread

from time import time

threads=[] #liste of threads

li=[]

def threadFunc(n):
    #function for test 
   for i in range(n):

       li.append(i)



n_threads=200 #for 200 core,  i tested this on server so  change it if you're using a computer 

for th in range(n_threads):
    #create n threads 
    process= Thread(target=threadFunc, args=[n_loop])
    process.start()
    threads.append(process)


x1=time()

for process in threads:
    process.join()

y1=time()


li=[]

x2=time()

threadFunc(n_loop*n_threads)

y2=time()



print("time with threads : ",y1-x1)

print("time without threads :", y2-x2)
from multiprocessing import Queue
import multiprocessing

def test(q) :
print q.qsize()

if __name__=="__main__"
q=Queue()

for i in range(100):
q.put(i)
p=multiprocessing.Process(target=test ,args(q, ))
p.start()
p.join()

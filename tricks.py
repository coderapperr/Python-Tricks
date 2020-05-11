'''Using Context Managers to calculate execution time of a function'''
from time import time, sleep
from contextlib import contextmanager

#context manager using class
class Timer:
	def __enter__(self):
		self.t1 = time()

	def __exit__(self, exc_type, exc_val, exc_tb):
		self.t2 = time()
		print('Execution Time: {} s'.format(self.t2-self.t1))

with Timer():
	sleep(1)

#context manager using function
@contextmanager
def Timer():
	try:
		t1 = time()
		yield 
	finally:
		t2 = time()
		print('Execution Time: {} s'.format(t2-t1))

with Timer():
	sleep(1)

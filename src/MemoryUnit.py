# @file         MemoryUnit.py
# @authors      Yihao

class MemoryUnit:
	'''
	This class implements a single-ported 256B memory Unit
	'''
	def __init__(self):
	'''
	Constructor for the memory unit

	@param memory A list representing the memory unit for each word
	@param flag A list representing if the corresponding word address is taken
	by float value
	@param memory_max_length An integar representing the maximum length of the 
	memory byte address
	'''
		self.memory = [0] * 64
		self.flag = [0] * 64
		self.memory_max_length = 256
	
	def mem_write(self, addr, value):
	'''
	Write value into certain memory address

	@param addr An integar representing the byte address to be written
	@param value An integar or float to be written
	'''
		if isinstance(value, int):		#int for 4 Bytes
			if addr > 256 or addr < 0:
				raise ValueError("Address value [ {} ] outrange in memory unit".format(addr))
			elif self.flag[int(addr/4)] != 0			#if the word is taken by a float
				tmp = self.flag[int(addr/4)]
				self.memory[int(addr/4)] = value
				self.memory[init(addr/4) + tmp] = 0	#clear the other word according to the value of flag
				self.flag[init(addr/4) + tmp] = 0
				self.flag[init(addr/4)] = 0
			else:
				self.memory[int(addr/4)] = value
		if isinstance(value, float):	#float for 8 Bytes
			if addr > 252 or addr < 0:
				raise ValueError("Address value [ {} ] outrange in memory unit".format(addr))
			else:
				self.memory[int(addr/4)] = value
				self.flag[int(addr/4)] = 1
				self.flag[int(addr/4)] = -1
	
	def mem_read(self, addr):
		return self.memory[int(addr/4)]

	def dump(self):
		print("Memory Unit".ljust(50, '=').rjust(80,'='))
		print("Memory content:")
		print(self.memory)
		print()


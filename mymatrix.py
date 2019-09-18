import copy

class MyMatrix:
	def __init__(self, data: list):
		"""
		Create matrix of given data.
		Example of data:
		[
			[1, 2, 3, 4],
			[5, 6, 7, 8],
		]
		Return TypeError if data is not list.
		"""
		if isinstance(data, list):
			self.__data = data
		else:
			raise ValueError
		#raise NotImplementedError

	def __repr__(self) -> str:
		"""
		Return visual presentation of matrix.
		Example:
		  1  20   3   4
		  5   6 100   8
		Hint: use '' for line break
		"""
		stri = ''
		for i in range(len(self.__data)):
			if i != 0 and i != len(self.__data):
				stri += '\n'
			for j in range(len(self.__data[i])):
				stri += str(self.__data[i][j]) + ' '
		return stri[:-1]
		#raise NotImplementedError


	def size(self) -> tuple:
		if len(self.__data) == 0:
			return (0, 0)
		else:
			return (len(self.__data), len(self.__data[0]))

		"""
		Return tuple(height, width) for matrix.
		Example: (2, 4)
		"""
		#raise NotImplementedError


	def flip_up_down(self):
		if self.size() == (0, 0): raise Exception('Матрица должна быть заполнена')

		for i in range(len(self.__data) // 2):
			self.__data[i], self.__data[-(i+1)] = self.__data[-(i+1)], self.__data[i]
		return self.__data

		"""
		E.g. modify
		1, 2, 3, 4   to   5, 6, 7, 8
		5, 6, 7, 8        1, 2, 3, 4
		"""
		#raise NotImplementedError

	def flip_left_right(self): 
		if self.size() == (0, 0): raise Exception('Матрица должна быть заполнена') 
		for i in range(len(self.__data)):
			for j in range(len(self.__data[i]) - 1):
				self.__data[i][j], self.__data[i][-(j+1)] = self.__data[i][-(j+1)], self.__data[i][j]
		return self.__data


		"""
		E.g. modify
		1, 2, 3, 4   to   4, 3, 2, 1
		5, 6, 7, 8        8, 7, 6, 5
		"""
		#raise NotImplementedError

	# методы flip_ ИЗМЕНЯЮТ матрицу
	# методы flipped_ по сути делают то же самое,
	# но возвращают изменённую КОПИЮ матрицы
	def flipped_up_down(self):
		if self.size() == (0, 0): raise Exception('Матрица должна быть заполнена')
		data = copy.deepcopy(self.__data)0:
		for i in range(len(data) // 2):
			data[i], data[-(i+1)] = data[-(i+1)], data[i][i]
		return data


		#raise NotImplementedError

	def flipped_left_right(self):
		if self.size() == (0, 0): raise Exception('Матрица должна быть заполнена')
		data = copy.deepcopy(self.__data)
		third = 0 
		if len(data) % 2 == 1:
			for i in range(len(data)):
				for j in range(len(data[i]) - 1):
					data[i][j], data[i][-(j+1)] = data[i][-(j+1)], data[i][j]
		else:
			medium = len(data) // 2 + 1
			for i in range(medium):
				for j in range(len(data[i])):
					data[i][j], data[i][-(j+1)] = data[i][-(j+1)], data[i][j]
		return data

		#raise NotImplementedError

	def transpose(self):
		if self.size() == (0, 0): raise Exception('Матрица должна быть заполнена')
		self.__data = [list(x) for x in zip(*self.__data)]
		return self.__data

		"""
		E.g. modify
						  1, 5
		1, 2, 3, 4   to   2, 6
		5, 6, 7, 8        3, 7
						  4, 8
		"""
		#raise NotImplementedError


	def transposed(self):
		data = copy.deepcopy(self.__data)
		data = [list(x) for x in zip(*data)]
		return data
		"""
		Return transposed copy of MyMatrix.
		"""
		#raise NotImplementedError


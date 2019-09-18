from mymatrix import MyMatrix
import pytest

def test_size():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.size() == (2, 3))
	matrix = MyMatrix([])
	assert(matrix.size() == (0, 0))

def test_flip_up_down():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.flip_up_down() == [[4, 5, 6], [1, 2, 3]])
	assert(repr(matrix) == '4 5 6 \n1 2 3')
	matrix = MyMatrix([[1, 2], [4, 5]])
	assert(matrix.flip_up_down() == [[4, 5], [1, 2]])
'''	matrix = MyMatrix([])
	assert(matrix.flip_up_down() == [])''' #проверила, что выкидывается ошибка

def test__repr():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(repr(matrix) == '1 2 3 \n4 5 6' )

def test_flip_left_right():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.flip_left_right() == [[3, 2, 1], [6, 5, 4]])
	assert(repr(matrix) == '3 2 1 \n6 5 4')
	matrix = MyMatrix([[1, 2], [3, 4], [5, 6]])
	assert(matrix.flip_left_right() == [[2, 1], [4, 3], [6, 5]])

def test_flipped_up_down():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.flipped_up_down() == [[4, 5, 6], [1, 2, 3]])
	assert(repr(matrix) == '1 2 3 \n4 5 6')
	matrix = MyMatrix([[1, 2], [4, 5]])
	assert(matrix.flipped_up_down() == [[4, 5], [1, 2]])

def test_flipped_left_right():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.flipped_left_right() == [[1, 2, 3], [4, 5, 6]])
	assert(repr(matrix) == '1 2 3 \n4 5 6')
	matrix = MyMatrix([[1, 2], [3, 4], [5, 6]])
	assert(matrix.flipped_left_right() == [[2, 1], [4, 3], [6, 5]])

def test_transpose():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.transpose() == [[1, 4], [2, 5], [3, 6]])
	assert(repr(matrix) == '1 4 \n2 5 \n3 6')
	matrix = MyMatrix([[1, 2], [3, 4], [5, 6]])
	assert(matrix.transpose() == [[1, 3, 5], [2, 4, 6]])

def test_transposed():
	matrix = MyMatrix([[1, 2, 3], [4, 5, 6]])
	assert(matrix.transposed() == [[1, 4], [2, 5], [3, 6]])
	assert(repr(matrix) == '1 2 3 \n4 5 6')
	matrix = MyMatrix([[1, 2], [3, 4], [5, 6]])
	assert(matrix.transposed() == [[1, 3, 5], [2, 4, 6]])

	
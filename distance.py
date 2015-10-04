# -*- coding:utf-8 -*-
import math

set = []

min_distance = 0
distance = 0
firstpoint = None
secondpoint = None
pair = None

N = 0

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast

class ShortNumbException(Exception):
    def __init__(self, value, minvalue):
        Exception.__init__(self)
        self.value = value
        self.minvalue = minvalue
		
class IntegerException(Exception):
    def __init__(self):
        Exception.__init__(self)

def main():
	print u"Данная программа для расчета минимального расстояния" \
		u" между двумя точками из введенного набора.\n" 
	while True:
		print u"Какое количество точек Вы хотите рассчитать?"
		try:
			N = input()
			if type(N) != int and type(N)==float:
				raise IntegerException()
			if N < 2:
				raise ShortNumbException(N, 2)
			break
		except NameError:
			print u"Необходимо ввести только одно число."
			pass
		except ValueError:
			print u"Необходимо ввести число." 
			pass
		except SyntaxError:
			print u"Необходимо ввести только одно число." 
			pass
		except EOFError:
			print u"Вы ввели пустое выражение."
			pass		
		except IntegerException:
			print u"Необходимо было ввести целое число, но введено дробное."
			pass
		except ShortNumbException as ex:
			print u"Количество точек для рассчета - {0}, а минимальное - {1}."\
			.format(ex.value, ex.minvalue)
			pass

	for i in range(N):
		while True:
			print u"Введите координаты", i+1, u"- й точки через пробел:"	
			try:
				pair = raw_input()
				pair = pair.split(" ")
				pair =[float(j) for j in pair]
				if len(pair)> 2:
					print u"Будут использованы первые две координаты."
				if len(pair) < 2:
					raise ShortInputException(len(pair), 2)
				set.append(pair)
				break
			except ShortInputException as ex:
				print u"Длина введённой строки равна {0}, а необходимо - {1}."\
				.format(ex.length, ex.atleast)
				pass
			except ValueError:
				print u"Необходимо ввести числа." 
				pass
		
	try:
		min_distance = math.sqrt((set[0][0]-set[1][0])**2 \
		+ (set[0][1]-set[1][1])**2)
	except IndexError:
		print 

	for key, pair in enumerate(set):
		if key < len(set)-1:
			distance = math.sqrt((pair[0]-set[key+1][0])**2 \
			+ (pair[1]-set[key+1][1])**2)
			if  distance < min_distance :
				min_distance = distance
	if len(set)!=0:
		print u'Результат:'
		if math.modf(min_distance)[0] == 0.0:
			print int(min_distance)
		else:
			print min_distance
		
main()
# создай список с целыми числами произвольных значений произвольной длины, 
>>> testList = [4, 8, 15, 23, 16, 42]

# отсортируй его по возрастанию и убыванию, запиши результат в отдельные переменные
testList.sort()
ASC = testList

testList.sort(reverse = True)
DESC = testList

# даны два списка с числами, нужно вернуть список, который состоит из общих чисел
a = [1, 4, 5, 7, 23, 36, 67, 78, 99, 134, 142, 150]
b = [3, 5, 6, 19, 67, 77, 123, 134, 172, 323, 434]

result = list(set(a) & set(b))

# напиши функцию, которая складывает сумму двух чисел, переданных ей на вход
 def Sum(x,y):
     m = x + y
     print(m)
# напиши функцию, которая возвращает тип данных, переданный ей на вход, и возвращает его на русском языке (пример: "строка")
def myType(a):
 	if type(a) == list:
 		print('это список')
 	elif type(a) == set:
 		print('это множество')
 	elif type(a) == int:
 		print('это целое число')
 	elif type(a) == float:
 		print('это дробное число')
 	elif type(a) == str:
 		print('это строка')
 	elif type(a) == dict:
 		print('это словарь')
 	elif type(a) == tuple:
 		print('это кортеж')
 	elif type(a) == bool:
 		print('это буль')
 	else:
		print('Нет такого типа')
# напиши функцию, которая принимает на вход любое количество чисел и говорит, есть ли среди них четное
vhod = [1,3,4,5,7,9,5,5,5,3]
isEven = False
for i in vhod:
	if i % 2 == 0:
		isEven = True
		break
		
if isEven:
	print('есть четные')
else:
	print('нет четных')
	
#2 способ

for i in vhod:
	if i % 2 == 0:
		print('есть четные')
		break
else:
	print('нет четных')

# используй тернарный оператор, чтобы вызвать функцию, если возраст больше 21 года, в противном случае верни сообщение "мы не продаем алкоголь несовершеннолетним"
age = 17
sell_alcohol()
sell_alcohol() if age > 21 else print('Мы не продаем алкоголь несовершеннолетним')
# загрузи список ключевых слова из модуля keyword, преобразуй его в строку со словами, разделенными запятой
import keyword
print (', '.join(keyword.kwlist))

# напиши функцию, которая проверит, является ли строка ключевым словом, используй модуль keyword
a = 'входные данные'
print(keyword.iskeyword(a))
# не забудь сначала изучить этот модуль с помощью dir, чтобы узнать, есть ли там полезные методы
print(dir(keyword))

# посчитайте, сколько раз символ встречается в строке, функция принимает на вход символ и строку
string = "I love apples, apple are my favorite fruit"
symbol = 'a'

def howMany(x,y):
	count = x.count(y)
	print(count)

howMany(string, symbol)

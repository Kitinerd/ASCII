# Вывод ASCII-кода символов латинского алфавита. Andrey Kopilevich - 2020 year;
import string
a=string.ascii_letters
for i in a:
	print(i + '=' + str(ord(i)))
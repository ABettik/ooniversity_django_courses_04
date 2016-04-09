#-*- coding: utf-8 -*-
from django.shortcuts import render

def quadratic_results(request):
	str_a = str_b = str_c = str_d = a = b = c = d = results = ''
	try:	
		a = int(request.GET['a'])
	except ValueError:
		if request.GET['a'].isalpha():
			a = request.GET['a']
			str_a = 'Коэффициент не целое число'
		else:
			str_a = 'Коэффициент не определен'
	
	try:	
		b = int(request.GET['b'])
	except ValueError:
		if request.GET['b'].isalpha():
			b = request.GET['b']
			str_b = 'Коэффициент не целое число'
		else:
			str_b = 'Коэффициент не определен'
	try:	
		c = int(request.GET['c'])
	except ValueError:
		if request.GET['c'].isalpha():
			c = request.GET['c']
			str_c = 'Коэффициент не целое число'
		else:
			str_c = 'Коэффициент не определен'
	if str_a == str_b == str_c == '': 
		if a == 0:
			str_a = 'Коэффициент при первом слагаемом уравнения не может быть равным нулю'
		else:
			d = b ** 2 - 4 * a * c
			if d > 0:
				str_d = 'Дискриминант: %d' % d
				x1 = (-b + d ** (1/2.0)) / (2*a)
				x2 = (-b - d ** (1/2.0)) / (2*a)
				results = 'Квадратное уравнение имеет два действительных корня: x1 = %.1f, x2 = %.1f' % (x1, x2)
			elif d < 0:
				str_d = 'Дискриминант: %d' % d
				results = 'Дискриминант меньше нуля, квадратное уравнение не имеет действительных решений.'
			else:
				str_d = 'Дискриминант: %d' % d
				x = -b / 2*a
				results = 'Дискриминант равен нулю, квадратное уравнение имеет один действительный корень: x1 = x2 = %.1f' % x
 
	return render(request, 'results.html',{'a':a, 'b':b,'c':c, 'str_a':str_a, 'str_b':str_b, 'str_c':str_c, 'str_d':str_d, 'results':results})

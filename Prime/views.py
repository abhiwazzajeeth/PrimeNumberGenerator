from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def Sieve(num):
	primes = []
	primes_range = [1 for i in range(num + 1)]
	i = 2
	while (i * i <= num):
		if(primes_range[i] == 1):
			for j in range(i * 2, num + 1, i):
				primes_range[j] = 0
		i = i + 1
	for i in range(2, num): 
		if primes_range[i]: 
			primes.append(i)
	return primes

def home(request):
	num = 0
	primes = []
	if request.GET.get('number'):
		number = request.GET.get('number')
		num = int(number)
		primes = Sieve(num)
	return render(request, 'index.html', {'number': num,'primes': primes})
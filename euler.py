#!/usr/bin/python

#Problem 1
#Find the sum of all numbers multiples of 3 or 5 below 1000
#Answer: 233168
def multipleSum():
	soma = 0;
	for i in range(1000-1):
		mult = i+1;
		if(mult%3==0 or mult %5==0):
			soma = soma + mult;
	return soma;

#Problem 2
#Find the sum of the even-valued terms on Fibonacci sequence where the fibonacci value is less than 4 milions.
#Answer: 4613732
def fib(n):
	if(n == 0 or n == 1):
		return n
	else:
		return (fib(n-1)+fib(n-2))

def problem2():
	fibval = 0
	soma = 0
	cont = 0
	while(fibval < 4000000):
		fibval = fib(cont);
		if(fibval % 2==0):
			soma = soma + fibval
		cont = cont + 1
	return soma

#Problem 7
#Find the sum of the 10001st first primes
#Answer: 104743
def primeNumber(n):
	primeCount=6
	number = 13
	lastPrime = 13
	flag = True
	while(primeCount != n):
		number+=1
		for i in range (number-1,2,-1):
			if(number%i==0):
				flag = False
				break
		if(flag):
			lastPrime = number;
			primeCount+=1
		else:
			flag = True

	return lastPrime

print(problem2())

raw_input("\n\nPress enter to exit");
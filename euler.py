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

#Problem 36
#Find the sum of all numbers less than one million which are palindromic in base 10 and base 2
#Answer: 872187
def problem36():
	cont = 0
	soma = 0;
	
	while(cont<1000000):
		#if cont equals to it's inverse (String)
		if(str(cont) == str(cont)[::-1]):
			#if cont (binarie) is equal to it's inverse (String)
			revbin = bin(cont)[2:]
			revbin = revbin[::-1]
			if(str(bin(cont)[2:]) == str(revbin)):
				soma = soma+cont;
		cont = cont + 1
	
	return soma;

#145: 1! + 4! +5! = 1 + 24 + 120 ==145
#Find the sum of all number with this caracteristc (The sum of the factorial is equal to the number)
#Answer: 40730
def factorial(n):
	fact = 0;
	if(n<=1):
		return 1
	
	fact = fact + n * factorial(n-1)
	return fact

def problem34():
	num = 10
	soma = 0
	soma2 = 0
	while(num <= 99999):
		soma=0
		numstr = str(num)
		for i in range(0, len(numstr), 1):
			fact = int(numstr[i])
			#Checked the hint on the forum. 9! is a large number. The factorial sum won get this far.
			if(fact<=8):
				soma = soma + factorial(fact)
				if(soma==num):
					soma2 = soma2 +soma


		num = num + 1
	return soma2



#Function Calls

#multipleSum()
#print(problem2())
#primeNumber(10001)
#print problem36()
#print (factorial(5))
#print factorial(6)
print problem34()
raw_input("\n\nPress enter to exit");
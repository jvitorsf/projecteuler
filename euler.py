def fibonacci(n):
	if(n ==0 or n==1):
		return n;
	else:
		return fibonacci(n-1) + fibonacci(n-2);

def primeNumber(n):
	primeCount=6;
	number = 13;
	lastPrime = 13;
	flag = True;
	while(primeCount != n):
		number+=1;
		for i in range (number-1,2,-1):
			if(number%i==0):
				flag = False;
				break;
		if(flag):
			lastPrime = number;
			primeCount+=1;
		else:
			flag = True;

	return lastPrime;

def recPrint(n):
	print n;
	if(n!=0):
		recPrint(n-1);

def foo1():
	try:
		number1 = int(raw_input("Enter a number: "));
		number2 = int(raw_input("Enter another number: "));
	except ValueError:
		print ("Not a number");
	
	sum = number1+number2;
	print sum;


foo1();
#print recPrint(1001);
raw_input("\n\nPress enter to exit");
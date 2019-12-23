#Write a program which contains one function named as Add() which accepts two numbers
#from user and return addition of that two numbers.
#Input : 11 5
#Output : 16



def Addfun(no1,no2):
	return no1+no2;

def main():
	no1=int(input("enter the first number"));
	no2=int(input("enter the second number"));

	iret=Addfun(no1,no2);
	
	print(iret);

if __name__=="__main__":
	main()

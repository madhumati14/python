#Write a program which contains one function named as ChkNum() which accept one
#parameter as number. If number is even then it should display “Even number” otherwise
#display “Odd number” on console.
#Input : 11
#Output : Odd Number
#Input : 8
#Output : Even Number

def add(no):
	if ((no%2)==0):
		print("no is even");
	else:
		print("no is odd");

def main():
	no=int (input("enter the number"));	
	add(no);

if __name__=="__main__":
	main()

#Write a program which accept number from user and check whether that number is positive or negative or zero.
#Input : 11
#Output : Positive Number
#Input : -8
#Output : Negative Number
#Input : 0
#Output : Zero

def Checkno(no):

	if (no>0):
		print("nober is positive");
	elif (no==0):
		print("nober is zero");
	else:
		print("number is negative");

def main():
	no=int (input("enter the number"))
	Checkno(no);	

if __name__=="__main__":
	main(); 

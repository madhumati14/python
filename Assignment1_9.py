#Write a program which display first 10 even numbers on screen.
#Output : 2 4 6 8 10 12 14 16 18 20

def DisplayEven():

	i=1;
	while i<=10:
		print(i*2,end=" ");
		i+=1;

def main():
	DisplayEven();

if __name__=="__main__":
	main();

'''

Factorial Again
Max. Marks100

Kate has finally calmed down and decides to forgive Little Deepu, but she won't forgive him just like that. She agrees to forgive him on the grounds that he can solve a mathematical question for her.
She gives Deepu a large number N and a prime number P and asks him to calculate ((3*N)! / (3!^N) ) (%) P.
Your task is to help Little Deepu get back together with Kate.

Input
First line contains number of test cases T.
Next T lines contain two integers N and P, where P is a prime.

Output
For each test case output the result ( (3*N)! / (3!)N ) (%) P. 

'''
def fact(a):
	fact = 1
	for i in range(1, a+1):
		fact=fact*i
	return fact

def main():
	tc  = int(raw_input())
	for i in range(0, tc):
		N, P = raw_input().split()
		N, P = int(N), int(P)
		print ((fact(3*N)/(pow(6,N)))%P)
main()
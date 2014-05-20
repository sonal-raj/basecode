# W(a,b) = MW(a) + MW(a+1) + MW(a+2)... + MW(b) (a and b both inclusive)
# where a and b are integers and MW is mini weird function, which is defined as:
# MW(i) = p^i + q^i + ... 
# where p and q (less than or equal to i) are all possible integers such that gcd(p,i) = p, gcd(q,i)= q ... and so on.
# For example:
# MW(10) = 1^10 + 2^10 + 5^10 + 10^10
# where gcd(1,10) = 1, gcd(2,10) = 2, gcd(5,10) = 5, gcd(10,10) = 10
# Your task is to find W(a,b) for given a and b.

def MW(n):
	result = 0
	for i in range(1,n+1):
		if n%i==0:
			result = result+pow(i,n)
	return result

def main():
	tc = int(raw_input())
	for i in range(0, tc):
		a, b = raw_input().split()
		a, b = int(a), int(b)
		result = 0
		for j in range(a,b+1):
			result = result+MW(j)
		print result%1000000007
main()

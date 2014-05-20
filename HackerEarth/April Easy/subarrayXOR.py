'''

Subarray XOR
Max. Marks100

Little Deepu since his breakup has been obsessed with XOR, so now he passes his time by calculating XOR of various numbers.
To help Little Deepu pass his time, his friend Rahul gives him an array of N numbers and asks him to calculate XOR of a range of numbers, from ath numbert to bth number (both a and b inclusive and are 0-based).

Input
The first line contains T, the number of test cases.
First line of each test case contains N, the number of elements in the array
Next line contains N integers, where ith integer is the ith element of the array
The line after that contains Q, the number of XOR queries to be performed on the array
Next Q lines each contain a and b, the range of indices for which XOR is to be calculated.

Output
For each query a, b you need to print
array[a] XOR array[a+1] XOR ... XOR array[b]

'''

def main():
	tc = int(raw_input())
	for i in range(0, tc):
		n = int(raw_input())
		num = list(map(int, raw_input().split()))
		xors = []
		xors.append(0)
		for i in range(0,n):			
				xors.append(num[i]^xors[i])

		#print num
		#print xors

		Q = int(raw_input())
		for j in range(0, Q):
			a, b = raw_input().split()
			a, b = int(a), int(b)
			print (xors[a]^xors[b+1])
main()


'''
never mind the code below

'''


def f(a):
	res = [a, 1, a+1, 0]
	return res[a%4]

def xor_finder():
	tc = int(raw_input())
	for i in range(0, tc):
		n = int(raw_input())
		num = list(map(int, raw_input().split()))
		Q = int(raw_input())
		for j in range(0, Q):
			a, b = raw_input().split()
			a, b = int(a), int(b)
			print (f(a-1)^f(b))

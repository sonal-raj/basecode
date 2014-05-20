'''
Game of numbers is a game where you are given two integers (X and Y), and you have to print the number of special numbers between X and Y both inclusive.
The property of a special numbers is as follows:
A special number is not divisible by any number of the form Z*Z where (Z>1).

Input:
T, the number of testcases. Each testcase consists of two space separated integers denoting X and Y.

Output: The required answer in one line for each testcase. 
'''

from math import sqrt
from math import ceil
def main():
	tc = int(raw_input())
	for loop in range(0, tc):
		x, y = map(int, raw_input().split())
		sq = []
		for i in range(2, int(ceil((y**0.5)))):
			sq.append(i*i)
		count = 0
		for i in range(x, y+1):
			flag=0
			for num in sq:
				if i%num==0:
					flag=1
					break
			if flag==0:
				#print i
				count=count+1
		print count
main()
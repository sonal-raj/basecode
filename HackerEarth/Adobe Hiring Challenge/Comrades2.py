'''
The army has n soldiers. The soldiers are numbers from 1 to n. The army has a superiority hierarchy. Every soldier has one immediate superior. 
The superior of a superior of a soldier is also a superior to that soldier. So, a soldier may have one or more superiors but only one immediate superior.
Every soldier has to congratulate every other soldier. For a pair of soldiers if one of them is the superior of the other, they will shake hands. Otherwise, they will bump their fists.

You are given the list of immediate superior of all soldiers. Your job is to tell how many handshakes and fist bumps will be there.

NOTE: Among all soldiers there is one soldier who does not have any superior. He is the commander of the whole army.

Input:

The first line of the input contains t, the number of test cases.
The first line of each test case contains n, the number of soldiers. The next line contains n space separated integers. The ith integer represents the immediate superior of the ith soldier.
The immediate superior of the commander of the army will be '0'.

Output:
Output two space separated integers, the number of handshakes and the number of fist bumps.

'''

def c2(n):
	return n*(n-1)/2

def main():
	tc = int(raw_input())
	for loop in range(0, tc):
		n = int(raw_input())
		ranks = list(map(int, raw_input().split()))
		
		freq = {}
		for num in ranks:
			if num in freq:
				freq[num]=freq[num]+1
			else:
				freq[num]=1
		#print freq

		fist = 0
		for k, v in freq.items():
			if v!=1:
				fist=fist+c2(v)

		print (c2(n)-fist), fist
main()
'''

A mind palace, according to Mr. Holmes is something that lets him retrieve a given memory in the least time posible. For this, he structures his mind palace in a very special way. 
Let a NxM Matrix denote the mind palace of Mr. Holmes. For fast retrieval he keeps each row and each column sorted. Now given a memory X, you have to tell the position of the memory
 in Sherlock's mind palace.

Input
Input begins with a line containing space separated N and M.
The next N lines each contain M numbers, each referring to a memory Y.
The next line contains Q, the number of queries.
The next Q lines contain a single element X, the memory you have to search in Sherlock's mind palace.

Output
If Y is present in Mr. Holmes memory, output its position (0-based indexing).
Else output "-1 -1" (quotes for clarity only).

'''

def main():
	N, M = map(int, raw_input().split())
	mem = []
	for i in range(0, N):
		mem.append(list(map(int, raw_input().split())))
	Q = int(raw_input())
	for i in range(0, Q):
		X = int(raw_input())
		
		xx = 0
		yy = M-1
		flag = 0
		while xx<N and yy>=0:
			if X>mem[xx][yy]:
				xx = xx+1
			else:
				if X<mem[xx][yy]:
					yy = yy-1
				else:
					print xx, yy
					flag = 1
					break
		if flag==0:
			print "-1 -1"
main()	
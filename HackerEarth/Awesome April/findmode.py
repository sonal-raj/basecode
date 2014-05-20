# Write a program to find the mode of a given list of integers.
# Mode of a number is defined as the number which is most frequently occured.
# For example: L = {1,2,2,3} // Here mode is 2(most frequently occured)
# It is possible that multiple answers are possible for a list.
# In that case print all possible answers in non decreasing order.

def main():
	tc = int(raw_input())
	for i in range(0, tc):
		n = int(raw_input())
		nums = list(map(int, raw_input().split()))
		hmap = {}
		for j in range(0,n):
			if nums[j] in hmap:
				hmap[nums[j]] = hmap[nums[j]]+1
			else:
				hmap[nums[j]] = 1
		# print hmap
		# traverse dict once to get max
		max = 0
		for k, v in hmap.iteritems():
			#print k, v
			if v>max:
				max=v
		# print max
		# traverse once to get those with max
		res=[]
		for k, v in hmap.iteritems():
			if(v==max):
				res.append(k)
		# print res
		#print the sorted list
		res.sort(reverse=True)
		restr = ""
		for ans in res:
			restr = restr+str(ans)+" "
		print restr
main()

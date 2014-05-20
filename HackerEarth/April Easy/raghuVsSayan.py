'''
Raghu and Sayan both like to eat (a lot) but since they are also looking after their health, they can only eat a limited amount of calories per day.
So when Kuldeep invites them to a party, both Raghu and Sayan decide to play a game. The game is simple, both Raghu and Sayan will eat the dishes served at the party 
till they are full, and the one who eats maximum number of distinct dishes is the winner. However, both of them can only eat a dishes if they can finish it completely i.e. 
if Raghu can eat only 50 kCal in a day and has already eaten dishes worth 40 kCal, then he can't eat a dish with calorie value greater than 10 kCal.
Given that all the dishes served at the party are infinite in number, (Kuldeep doesn't want any of his friends to miss on any dish) represented by their calorie value(in kCal) 
and the amount of kCal Raghu and Sayan can eat in a day, your job is to find out who'll win, in case of a tie print “Tie” (quotes for clarity).

Input:
First line contains number of test cases T.
Each test case contains two lines.
First line contains three integers A, B and N.
where A and B is respectively the maximum amount of kCal Raghu and Sayan can eat per day, respectively and N is the number of dishes served at the party.
Next line contains N integers where ith integer is the amount of kCal ith dish has.

Output:

For each test case print "Raghu Won" (quotes for clarity) if Raghu wins else if print "Sayan Won" (quotes for clarity) if Sayan wins else print "Tie" (quotes for clarity) if both eat 
equal number of dishes.

'''

def main():
	tc = int(raw_input())
	for i in range(0, tc):
		A, B, N = map(int, raw_input().split())
		cals = list(map(int, raw_input().split()))
		cnt1 = 0
		cnt2 = 0

		cals.sort()

		for i in range(0, N):
			if cals[i]<=A:
				A=A-cals[i]
				cnt1 = cnt1+1
			if cals[i]<=B:
				B=B-cals[i]
				cnt2=cnt2+1
		if cnt1>cnt2:
			print "Raghu Won"
		else:
			if cnt1<cnt2:
				print "Sayan Won"
			else:
				print "Tie"
main()
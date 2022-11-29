
def knapSack(W, wt, val, n):

	
	if n == 0 or W == 0:
		return 0


	if (wt[n-1] > W):
		return knapSack(W, wt, val, n-1)
	else:
		return max(
			val[n-1] + knapSack(
				W-wt[n-1], wt, val, n-1),
			knapSack(W, wt, val, n-1))


  



val = [91, 72, 90, 46, 55, 8, 35, 75, 61, 15, 77, 40, 63, 75, 29, 75, 17, 78, 40, 44]
wt = [84, 83, 43, 4, 44, 6, 82, 92, 25, 83, 56, 18, 58, 14, 48, 70, 96, 32, 68, 92]
W = 879
n = len(val)
print(knapSack(W, wt, val, n))


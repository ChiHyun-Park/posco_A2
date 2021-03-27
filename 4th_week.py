import sys
n= int(input())
budget=list(map(int,input().split()))
m=int(input())

result=0
start,end=0,max(budget)
while start<=end:
  mid=(start+end)//2
  total=0
  for i in budget:
    if i>=mid:
      total+=mid
    else:
      total+=i

  if total>m:
    end = mid-1
  else:
    start=mid+1
    if result<mid:
      result=mid



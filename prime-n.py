n=int(input())
for j in range(3,n):
  count=1
  for i in range(2,j):
    if j%i!=0:
      count=count + 1
      if count==j-1:
        print(j)
        break
    else:
      break

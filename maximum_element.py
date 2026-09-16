def rep(arr):
  freq={}
  for i in arr:
    if i in freq:
      freq[i]+=1
    else:
      freq[i]=1
  max_element=0
  max_count=0
  for i in freq:
    if max_count<freq[i]:
        max_count=freq[i]
        max_element=i
  print("max element: ",max_element)
  print("max count: ",max_count)
arr=[2, 5, 2, 8, 5, 2, 3, 5, 2]
rep(arr)
def rot(arr,k):
  k%=len(arr)
  return arr[-k:]+arr[:-k]
arr=[1, 2, 3, 4, 5]
k=int(input("enter: "))
print(rot(arr,k))
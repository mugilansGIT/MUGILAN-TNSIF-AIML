def lar(arr):
  largest=s_largest=arr[0]
  for i in arr:
    if i>largest:
      s_largest=largest
      largest=i
    elif i>s_largest and i!=largest:
      s_largest=i
  print("second largest:",s_largest)
arr=[1,2,34,45,6]
lar(arr)


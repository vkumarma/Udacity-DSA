def count_inversions(arr):  # using merge sort
  count = 0
  inversion = [count]
  tmp_arr = [0] * len(arr)
  start = 0
  end = len(arr) - 1
  
  def merge_sort(arr,tmp_arr,start,end):
    if start >= end:
      return
  
    mid = (start+end) // 2
    merge_sort(arr,tmp_arr,start,mid)
    merge_sort(arr,tmp_arr,mid+1,end)
    merge(arr,tmp_arr,start,mid,mid+1,end)
  
  def merge(arr,tmp_arr,start_one,end_one,start_two,end_two):
    i = start_one
    j = start_two
    k = start_one
    while i <= end_one and j <= end_two:
      if arr[i] > arr[j]:
        tmp_arr[k] = arr[j]
        inversion[0] += (end_one-i)+1
        k += 1
        j += 1
        
      else:
        tmp_arr[k] = arr[i]
        k += 1
        i += 1
  
    while i <= end_one:
      tmp_arr[k] = arr[i]
      k += 1
      i += 1
  
    while j <= end_two:
      tmp_arr[k] = arr[j]
      k += 1
      j += 1
  
    for a in range(start_one,end_two+1):
      arr[a] = tmp_arr[a]
  
    return 

  merge_sort(arr,tmp_arr,start,end)
  return inversion[0]


print(count_inversions([54, 99, 49, 22, 37, 18, 22, 90, 86, 33]))



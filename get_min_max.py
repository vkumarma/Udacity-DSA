import random
def get_min_max(arr):
  max = -float('inf')
  min = float('inf')
  i = len(arr) // 2
  while i <= len(arr) - 1:
    temp = len(arr) - 1 - i
    if arr[temp] > max and arr[temp] > arr[i]:
      max = arr[temp]
      
    elif arr[i] > max:
      max = arr[i]

    if arr[temp] < min and arr[temp] < arr[i]:
      min = arr[temp]

    elif arr[i] < min:
      min = arr[i]

    i += 1

  return min, max


l = [i for i in range(0, 10)]  # a list containing 0 - 9
m =  [i for i in range(5, 21)]
random.shuffle(l)
random.shuffle(m)

print ("Pass" if ((0, 9) == get_min_max(l)) else "Fail")
print ("Pass" if ((5, 20) == get_min_max(m)) else "Fail")


x = [1,2,3,4,5]

for i in x: # for each
  print(i)

for i in range (len(x)): #fpr loop
  print(i)

x = [10, 20, 30, 40, 50]
for i in x: # for each loop
    print(i)

for i in range (len(x)):  #for loop
    print(x[i])


# now you have to print their index at the same line using for loop.

for i in range(len(x)):
    # index, value
    print(f"Index: {i}, Value: {x[i]}")


#enumerate problem

for index,elem in enumerate(x):
    print(f"Index: {index}, Value: {elem}")



# Question 1 Two sum on neetcode 150

class solution:
  def twoSum(self, nums: List[int]m target : int) -? list[int]:
    seen = {}
    for index,num in enumerate(nums):
      diff = target - num
      if diff in seen:
        print([seen[diff], index)
      else:
        print([index])

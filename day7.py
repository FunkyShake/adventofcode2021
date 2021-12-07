# Part 1
with open('day7.py', 'r') as f:
  ls = list(map(int, f.read().strip().split(',')))
 
numbers = []
lists = []

for i in range(len(ls)):
  for line in ls:
    if ls[i] > line:
      numbers.append(ls[i] - line)
    else:
      numbers.append(line - ls[i])
  lists.append(numbers)
  numbers = []
    
for item in range(len(lists)):
  lists[item] = sum(lists[item])
lists.sort()
print(lists[:1])   

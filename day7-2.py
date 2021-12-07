# Part 1
with open('day7.txt', 'r') as f:
  ls = list(map(int, f.read().strip().split(',')))
 
numbers = []
lists = []
a = 0
b = 0

for i in range(len(ls)):
  for line in ls:
    if ls[i] > line:
      b = (ls[i] - line)
      numbers.append(sum([j for j in range(a, b+1))
    else:
      b = (line - ls[i])
      numbers.append(sum([j for j in range(a, b+1))
  lists.append(numbers)
  numbers = []
    
for item in range(len(lists)):
  lists[item] = sum(lists[item])
lists.sort()
print(lists[:1])  

# Part 2
with open('day7.txt', 'r') as f:
  ls = list(map(int, f.read().strip().split(',')))
 
numbers = []
lists = []
a = 0
b = 0

ls.sort()
for line in ls:
  for i in range(ls[0], (ls[-1]+1)):

    if line > i:
      b = (line - i)
      numbers.append(sum([j for j in range(a, b+1)]))
    else:
      b = (i - line)
      numbers.append(sum([j for j in range(a, b+1)]))
  lists.append(numbers)
  numbers = []
   
results = list(zip(*lists))
for item in range(len(results)):
  results[item] = sum(results[item])

results.sort()
print(results[:1])

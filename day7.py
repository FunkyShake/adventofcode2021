# Part 1
with open('day7.py', 'r') as f:
  ls = list(map(int, f.read().strip().split(',')))
 
numbers = []
lists = []

for i in range(len(ls)):
  for line in ls:
    if ls[i] > x:
      numbers.append(ls[i] - x)
    else:
      numbers.append(x - ls[i])
    lists.append(numberino)
    numberino = []
    
results = list(zip(*lists))
for item in range(len(results)):
  results[item] = sum(results[item])
  
results.sort()

print(results[:1])    

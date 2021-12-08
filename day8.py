with open('day8.txt', 'r') as f:
  ls = f.read().strip().split('\n')
  
count = 0

splitls = [len(word) for line in ls for word in line.split(' | ')[1].split(' ')]

for item in splitls:
  if item == 2 or item == 3 or item == 4 or item == 7:
    count += 1
    
  else:
    pass
  
print(count)

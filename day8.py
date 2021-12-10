from itertools import permutations # for part 2

# part 1
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

# part 2
totals = 0
# set example in integer order 0-9
example = ["abcefg", "cf", "acdeg", "acdfg", "bcdf", "abdfg", "abdefg", "acf", "abcdefg", "abcdfg"]
ex_set = set(example)

for line in ls:
    left, right = line.split(' | ')
    
    for perm in permutations("abcdefg"):
      
      #making a dictionary of every letter combination
      dictionaries = {k: v for k, v in zip(perm, 'abcdefg')}
      
      # making a set of possible dictionary combinations
      l = {''.join(sorted(map(dictionaries.get, item))) for item in left.split()}
      
      if l == ex_set:
        
        # make a list of dictionary items for right side
        right = [''.join(sorted(map(dictionaries.get, item))) for item in right.split()]
        # make a string based off the index in example
        right = ''.join(str(example.index(x)) for x in right)
        # convert to integer and add to totals
        totals += int(right)
                        
print(totals)

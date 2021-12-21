# First one I can conceivably do in a while... hooray for Brute Force!

p1_pos = 1
p2_pos = 5

p1_score = 0
p2_score = 0

dice = 1
dice_roll = 0

while p1_score < 1000 or p2_score < 1000:
  roll = sum([d for d in range(dice, dice+3)])
  
  if roll + p1_pos <= 10:
    p1_score += p1_pos+roll
    p1_pos = p1_pos+roll
  
  # modulo operator '%' lets us ignore the dice rolling back over
  elif (roll + p1_pos) % 10
    p1_score += 10
    p1_pos = 10
  
  else:
    p1_score += (roll + p1_pos) % 10
    p1_pos = (roll + p1_pos) % 10

  dice_roll += 3
  dice += 3  
  # i'm not super fancy so here's a break just in case it happens before we get back to start
  if p1_score >= 1000:
    print(p2_score * dice_roll)
    break
  else:
    pass
  
  roll = sum([d for d in range(dice, dice+3)])
  if roll + p2_pos <= 10:
    p2_score += p2_pos+roll
    p2_pos = p2_pos+roll
  
  elif (roll + p2_pos) % 10
    p2_score += 10
    p2_pos = 10
  
  else:
    p2_score += (roll + p2_pos) % 10
    p2_pos = (roll + p2_pos) % 10
  
  #dice roll is counted before breaking
  dice_roll += 3
  dice += 3    
  # i'm not super fancy so here's a break just in case it happens before we get back to start
  if p2_score >= 1000:
    print(p1_score * dice_roll)
    break
  else:
    pass  

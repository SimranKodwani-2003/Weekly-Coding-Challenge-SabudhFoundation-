def successfulPairs(spells, potions, success):
    potions.sort()
    pairs = []

    for i in range(len(spells)):
      for j in range(len(potions)):
        if spells[i] * potions[j] >= success:
          pairs.append(len(potions) - j)
          break
        elif j == len(potions) - 1:
          pairs.append(0)
    return pairs

spells = [3,1,2]
potions = [8,5,8]
success = 16
print(successfulPairs(spells, potions, success)) 

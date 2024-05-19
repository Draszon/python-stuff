playerOne = input("Add meg az első játékos nevét: ")
playerTwo = input("Add meg a második játékos nevét: ")
print("Most pedig add meg melyik játékot szeretnéd játszani")
gameType = input("301 vagy 501: ")

while gameType != "301" and gameType != "501" or not gameType.isdigit():
  gameType = input("Helytelen érték, add meg újra: ")

gameType = int(gameType)
print("{}-es játékot választottad! Jó játékot {} és {}!".format(gameType,playerOne,playerTwo), end='\n\n')
playerOneScore = gameType
playerTwoScore = gameType

def scoreCalculator(playerName, playerScore):
  print("\n{} jön, {}-pontnál jársz!".format(playerName, playerScore))
  throwCounter = 1
  currentTotal = 0
  while throwCounter <= 3:
    currentThrow = input("{}. dobás eredménye: ".format(throwCounter))

    while not currentThrow:
      currentThrow = input("{}. dobás eredménye: ".format(throwCounter))

    if currentThrow.startswith('d'):
      currentThrow = int(currentThrow[1:]) * 2
      currentTotal += currentThrow
      throwCounter += 1
      if playerScore - currentTotal <= 0:
        break
    elif currentThrow.startswith('t'):
      currentThrow = int(currentThrow[1:]) * 3
      currentTotal += currentThrow
      throwCounter += 1
      if playerScore - currentTotal <= 0:
        break
    else:
      currentThrow = int(currentThrow)
      currentTotal += currentThrow
      throwCounter += 1
      if playerScore - currentTotal <= 0:
        break

  if playerScore - currentTotal < 0:
    return playerScore
  elif playerScore - currentTotal >= 0:
    return playerScore - currentTotal
  else:
    print("Valami hiba történt!")

while playerOneScore != 0 and playerTwoScore != 0:
  playerOneScore = scoreCalculator(playerOne, playerOneScore)
  if playerOneScore == 0:
    print("Gratulálok {}! Megnyerted a játékot!".format(playerOne))
    break
  elif playerOneScore > 0:
    print("{} pontod maradt!".format(playerOneScore))
  else:
    print("Valami hiba történt!")

  playerTwoScore = scoreCalculator(playerTwo, playerTwoScore)
  if playerTwoScore == 0:
    print("Gratulálok {}! Megnyerted a játékot!".format(playerTwo))
    break
  elif playerOneScore > 0:
    print("{} pontod maradt!".format(playerTwoScore))
  else:
    print("Valami hiba történt!")
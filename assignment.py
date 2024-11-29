while True:
  try: 
    x = int(input())
    y = 0
    if x < 1:
      print ("Input a greater number")
    else:
      for i in range(x):
        if i % 2 == 0:
          y = y + 1 / (2 * i + 1)
        else:
          y = y - 1 / (2 * i + 1)
      y = y * 4

      print (round(y, 3))
  except ValueError:
    print ("Please enter a valid number")


#def calculatePi(digits):
  #result = 0 
  #return result

#number_of_digits = input()
#print(calculatePi(number_of_digits))

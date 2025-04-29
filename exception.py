newList = [2,4,6, 'California']

for element in newList:
    try:
        print(element/2)
    except:
        print(newList[3])
        
  
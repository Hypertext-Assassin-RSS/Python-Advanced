import re

class Reg:
    def checkRegEx():
        input('Enter Number :')


    name = 'Rajith Sanjaya'
    #check the given string present in the string
    # r = 'raw'
    if(re.findall(r'Sanjaya',name)):
        print('word in the string')
    else:
        print('word is not dound in the string!')

    #find all the number chrachters in given string 
    address = 'no 69 sahanagama wikkala'
    print(re.findall(r'\d',address))

    #add modifyer to fix the sepereation of the numbers
    print(re.findall(r'\d+',address))


    if(re.search('Sanjaya',name)):
        print('Found !')
    else:
        print('not found')

    #split the word at given char
    split = re.split(r'j',name)
    print(split)
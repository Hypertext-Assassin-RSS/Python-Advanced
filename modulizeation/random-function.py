import random

#print random number 
print('Random Number :',random.random())

print('Random Randrange Number :',random.randrange(10,100,5))

print('Random Randit Number :',random.randint(1,10))

list = [1,6,8,3,10,25,68]
random.shuffle(list)
print('Shuffeled List : ',list)

numLis = [151,251,351,451,551]
print(random.choices(numLis,weights=(10,20,30,40,50),k=5))


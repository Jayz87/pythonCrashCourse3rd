magicians=["Harry","Hermoine","Ron"]
for magician in magicians:
    print(magician)

pizzas=["pepperoni","pineapple","veg"]    
for pizza in pizzas:
    print(f'I like {pizza} pizza the best' )
print("i really love my pizza")    

pets=["dog","calf","hamster"]    
for pet in pets:
    print(f'{pet} makes the best pet' )
print("All are cute pets")

for value in range(1,5):
    print(value)

even_numbers= list(range(2,21,2))
print(even_numbers)

squares=[]
for value in range(1,11):
    #square = value**2
    squares.append(value **2)
print(squares) 

digits=list(range(10,100))
print(min(digits))
print(max(digits))
print(sum(digits))

#list comprehensions
squares2=[value**2 for value in range(1,11)]
print(squares2)

wizards=[wiz+"ji" for wiz in magicians]
print(wizards)

#4.3
for num in range(1,21):
    print(num)
#4.4
#for num in range(1,10_00_001):
 #   print(num) 

#4.5
mill_numbers= list(range(1,10_00_001))
print(min(mill_numbers))
print(max(mill_numbers))
print(sum(mill_numbers))

#4.6
oddnumbers=[val for val in range(1,20,2)]
print(oddnumbers)
#4.7
multiples_of_three =[val*3 for val in range(1,11)]
print(multiples_of_three)

#4.8,4.9 cubes
print('cubes')
cubes=[value**3 for value in range(1,11)]
print(cubes)
print(cubes[-3:])

print("cubugal is a copy of cubes")
cubugal =cubes[:]
cubugal.append("gkhkj")
print(cubugal)  

split_wiz=magicians[1:]
for wiz in split_wiz:
  print(f'{wiz} is my fav wizard')

#list values are changeable but tuples are not . 


    
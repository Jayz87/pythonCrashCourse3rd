dimensions =(50,20)
print(dimensions[0])
print(dimensions[1])

# dimensions[0]=30 is not allowed but below is allowed
dimensions=(40,60)
for dim in dimensions:
    print(dim)

#4.13    
buffet=("starters","main","desserts")
for buf in buffet:
    print(buf)

#buffet[0]="soups"   
buffet=("soups","rice","payasam")
for buf in buffet:
    print(buf) 

if "soups"in buffet:
    print("soup is available")
if "salad" in buffet:
    print("salad is available")
else:
    print("Our salad is in demand, better luck next time")       
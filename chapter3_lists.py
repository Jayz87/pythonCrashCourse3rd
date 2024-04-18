names=["harry","darcy","martin"]
print(names[0].title())
print(names[1].title())
print(names[-1].title())
print(names)
print(f'Hi {names[0]} do visit our home')
print(f'Hi {names[1]} do visit our home')
print(f'Hi {names[2]} do visit our home')

transport=['bike','yatch','car']
brand=["honda","Ducati"]
print(f'I would like to ride a {brand[0]} {transport[1]}' )

names.remove("harry")
names.append("kar")
names.insert(0,"captain America")
names.insert(2,"bruce")
names.insert(3,"iron man")
popped_name = names.pop(2)
del names[-2]
print(f'Hi {names[0]} do visit our home for dinner')
print(f'Hi {names[1]} do visit our home for dinner')
print(f'Hi {names[2]} do visit our home for dinner')
print(f'Hi {names[len(names)-1]} do visit our home for dinner')
print(names)
print(popped_name)

names.sort(reverse=True)
print(names)

names.reverse()
print(names)
print(len(names))
#just learn dictionary
buff = ['attack boost', 'defense boost', 'poison debuff']

#we can put anything in the value. list, int, float, bool, even another dictionary
skills = {
    'normal attack' : 'wind sphere',
    'normal skill' : 'wind spear',
    'weapon skill' : 'Galeweave',
    'ultimate skill' : 'tempest',
    'buff' : buff
}
print(skills)

#dict length
skillen = len(skills)
print(skillen)

#check if exist
key = 'normal attack'
checkkey = key in skills    
print(checkkey)

#read dict
print(skills['normal attack'])

#read dict using get
print(skills.get('normal attack'))

#difference is, when using get, if the key is not present, it will throw None instead of an error
#print(skils['4th attack']) -> error
#print(skils.get('4th attack')) -> None
#kinda like print + check if exist

#update and add dict
skills.update({'normal attack' : 'bloody cleave'})
#add kalau ga ada
skills.update({'active' : True})

#ambil iterable items:
#ambil value skills.values()
#ambil keys skills.keys()
#ambil items skills.items()

#loop
for skill in skills:
    #yang keluar = key
    print(skill)

#ambil key
for skill in skills.keys():
    #yang keluar = value
    print(skills.get(skill))

#loop keluar value jg
for skill in skills.values():
    print(skill)

#loop keluar keys jg
for skill in skills.keys():
    print(skill)

#keluarannya pasangan tuple
for skill in skills.items():
    print(skill)

#bisa gini juga, pisah gitu
for key, value in skills.items():
    print(f'{key} = {value}')

#pop
normal_skill = skills.pop('normal skill')
print(normal_skill)
print(skills)
#bisa pop items terakhir dengan skills.popitem()

import datetime

comic1 = {
    'title' : 'Overgeared',
    'total_chapter' : 179,
    'genres' : ['Action', 'Fantasy', 'Adventure', 'Comedy'],
    'last_updated' : datetime.datetime(2023, 12, 22, 19, 48)
}

comic2 = {
    'title' : 'The World After The End',
    'total_chapter' : 107,
    'genres' : ['Action', 'Fantasy', 'Adventure', 'Shounen'],
    'last_updated' : datetime.datetime(2023, 12, 28, 1, 5)
}

comics = {
    'C1' : comic1,
    'C2' : comic2
}

for comic in comics:
    KEY = comic
    title = comics[KEY]['title']
    total_chapter = comics[KEY]['total_chapter']
    genres = comics[KEY]['genres']
    last_updated = comics[KEY]['last_updated'].strftime("%x")
    print(f"{KEY:<5}{title:<25}{total_chapter:<5}{genres}\t{last_updated:<10}")

#learn *args
#its like pointer to an array in cpp tbh, but for function and it doesnt have to be a declared array
def add(*args):
    out = 0

    for num in args:
        out += num

    return out

print(add(2, 3, 4, 6, 1, 1, 9, 9, 2))
print(add(9, 9, 2))

#this prints out dictionary somehow
def stuff(**kwargs):
    print(kwargs)

    #bisa gini buat print langsung (static)
    print(kwargs['a'])
    print(kwargs['b'])
    print(kwargs['c'])
    print(kwargs['d'])

    #gini buat anuin keys
    for arg in kwargs.keys():
        print(arg)

    #gini buat value
    for arg in kwargs.values():
        print(arg)

    #pake items juga bisa

stuff(a='why', b='is', c=10, d='ten')

#kwargs
def meth(*args, **kwargs):
    out = args[0]
    if kwargs['options'] == 'add':
        for num in args[1:]:
            out += num

    elif kwargs['options'] == 'subtract':
        for num in args[1:]:
            out -= num

    elif kwargs['options'] == 'times':
        for num in args[1:]:
            out *= num

    elif kwargs['options'] == 'divide':
        for num in args[1:]:
            out /= num 

    return out

print(meth(10, 5, 2, options='add'))     
print(meth(10, 5, 2, options='subtract'))
print(meth(10, 5, 2, options='times'))
print(meth(10, 5, 2, options='divide'))
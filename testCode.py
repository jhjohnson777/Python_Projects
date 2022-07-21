


mySentence = 'loves the color'

color_list = ['red', 'blue', 'pink', 'black', 'orange']

def color_function(name):
    list = []
    for i in color_list:
        msg = '{} {} {}'.format(name, mySentence, i)
        list.append(msg)
    return list

def get_name():
    go = True
    while go:
        name = input('What is your name? ')
        if name == '':
            print('you need to provide your name')
        elif name == 'Sally':
            print('Sally, you cant use this software.')
        else:
            go = False
    list = color_function(name)
    for i in list:
        print(i)

get_name()

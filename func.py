def thing():
    print('Hello')

print('There')


x = 'banana'
y = max(x)
print(y)


def func(x):
    print(x)

func(10)
func(20)


def stuff():
    print('Hello')
    return
    print('World')

stuff()



def greet(lang):
    if lang == 'es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

print(greet('fr'),'Michael')


def addtwo(a, b):
    added = a + b
    return a

x = addtwo(2, 7)
print(x)

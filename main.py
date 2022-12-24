class Person:
    def __init__(self, name, health, coordinate):
        self.name = name
        self.health = health
        self.coordinate = coordinate
health = (100)
x=0
y=0
coordinate = ((x), (y))
y1=0
x1=0
coordinate2 = ((x1),(y1))
name = input('Введите имя персонажа: ')
print('Ваше имя ', name)
print('Ваше здоровье', health)
print('Вы находитесь в точке ', coordinate)
coordinatemove = input( 'Чтобы переместить персонажа в другую точку оси x напишите right или left, оси y напишите up или down:')
# if coordinatemove:
#     coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
# if coordinatemove == 'up' or 'down' or 'left' or 'right':
#         coordinatemove = input( 'Чтобы переместить персонажа в другую точку оси x напишите right или left, оси y напишите up или down:')

while coordinatemove == 'up':
    if y <= 10000:
        y+= 1
        y1=y-1
        print('Персонаж', name, 'переместился из точки ', '(',(x1),',',y1,')',',в точку ', '(',(x),',',y,').Текущее здоровье 100.' )
        coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))

# while coordinatemove != 'up':
while coordinatemove == 'down':
    if y <= 10000:
        y-= 1
        y1=y+1
    print('Персонаж', name, 'переместился из точки ','(',(x1),',',y1,')', ',в точку ', '(', x, ',', y, ').Текущее здоровье 100.')
    coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
while coordinatemove == 'left':
    if x <= 10000:
        x-= 1
        x1=x+1
    print('Персонаж', name, 'переместился из точки ', '(',(x1),',',y1,')', ',в точку ', '(', x, ',', y, ').Текущее здоровье 100.')
    coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
while coordinatemove == 'right':
    if x <= 10000:
        x+= 1
        x1=x-1
    print('Персонаж', name, 'переместился из точки ','(',(x1),',',y1,')', ',в точку ', '(', x, ',', y, ').Текущее здоровье 100.')
    coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
while coordinatemove:
        coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
        # if coordinatemove == 'up' or 'down' or 'left' or 'right':
        #     coordinatemove = input( 'Чтобы переместить персонажа в другую точку оси x напишите right или left, оси y напишите up или down:')
        while coordinatemove == 'up':
            if y <= 10000:
                y += 1
                y1 = y - 1
                print('Персонаж', name, 'переместился из точки ', '(', (x1), ',', y1, ')', ',в точку ', '(', (x), ',',
                      y, ').Текущее здоровье 100.')
                coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))

        # while coordinatemove != 'up':
        while coordinatemove == 'down':
            if y <= 10000:
                y -= 1
                y1 = y + 1
            print('Персонаж', name, 'переместился из точки ', '(', (x1), ',', y1, ')', ',в точку ', '(', x, ',', y,
                  ').Текущее здоровье 100.')
            coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
        while coordinatemove == 'left':
            if x <= 10000:
                x -= 1
                x1 = x + 1
            print('Персонаж', name, 'переместился из точки ', '(', (x1), ',', y1, ')', ',в точку ', '(', x, ',', y,
                  ').Текущее здоровье 100.')
            coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
        while coordinatemove == 'right':
            if x <= 10000:
                x += 1
                x1 = x - 1
            print('Персонаж', name, 'переместился из точки ', '(', (x1), ',', y1, ')', ',в точку ', '(', x, ',', y,
                  ').Текущее здоровье 100.')
            coordinatemove = input(str('Напишите куда дальше хотите переместиться:'))
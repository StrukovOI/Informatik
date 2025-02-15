import functools

def exist(cls):                     # Декоратор класса
    def ex(self):
        print(f"{self._type} является многоугольником с четырьмя сторонами")
    cls.ex = ex
    return cls

class polygon:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour

@exist
class quadrilateral(polygon):
    def __init__(self, name, colour, type, a, b):
        super().__init__(name, colour)
        self._type = type
        self._polygon_sqare = 'Квадрат'
        self._polygon_rectangle = 'Прямоугольник'
        self._polygon_romb = 'Ромб'
        self._a = a
        self._b = b
        
    
    def info(self):
        print(f'Класс предмета: {self.name}, Тип: Четырёхугольник, Цвет: {self.colour}')

    @property  
    def a(self):
        return self._a
    @property  
    def b(self):
        return self._b
    
    @a.setter
    def a(self, new_a):              # Методы, позволяющие менять длины сторон только на бóльшие по значению
        if new_a >= self._a:
            self._a = new_a
            self.sq_sqare = self._a*self._b
            self.sq_rectangle = self._a*self._b
            self.sq_romb = self._a*self._b

    @b.setter
    def b(self, new_b):
        if new_b >= self._b:
            self._b = new_b
            self.sq_sqare = self._a*self._b
            self.sq_rectangle = self._a*self._b
            self.sq_romb = self._a*self._b

    def extra_info(self):
        if self._type == 'Квадрат':
            print(f'Подтип: {self._polygon_sqare}, Количество углов: 4, Сторона = {self._a}, Площадь S = {self._a*self._b}\n')
        elif self._type == "Прямоугольник":
            print(f'Подтип: {self._polygon_rectangle}, Количество углов: 4, Стороны = {self._a} и {self._b}, Площадь S = {self._a*self._b}\n')
        elif self._type == "Ромб":
            print(f'Подтип: {self._polygon_romb}, Количество углов: 4, Сторона = {self._a}, Площадь S = {self._a*self._b/2}\n')

squar = quadrilateral('Геометрическая фигура', 'Белый', 'Квадрат', 10, 10)
rect = quadrilateral('Геометрическая фигура', 'Красный', 'Прямоугольник', 3, 4)
ro = quadrilateral('Геометрическая фигура', 'Синий', 'Ромб', 4, 4)

squar.info()
squar.extra_info()
rect.info()
rect.extra_info()
ro.info()
ro.extra_info()

squar.a = 20
squar.b=20
squar.extra_info()

squar.a=5
squar.b=5
squar.extra_info()

rect.a=11
rect.b=28
ro.a=1
ro.b=1

rect.extra_info()
ro.extra_info()

squar.ex()

class polygon:
    def __init__(self, name, colour):
        self.name = name
        self.colour = colour
        
class quadrilateral(polygon):
    def __init__(self, name, colour, type):
        super().__init__(name, colour)
        self.type = type
        self.sq_sqare = 'a\u00B2'
        self.sq_rectangle = 'a*b'
        self.sq_romb = 'a*b*sin(\u03B1)'
        self.polygon_sqare = 'Квадрат'
        self.polygon_rectangle = 'Прямоугольник'
        self.polygon_romb = 'Ромб'

    def info(self):
        print(f'Класс предмета: {self.name}, Тип: Четырёхугольник, Цвет: {self.colour}')

    def extra_info(self):
        if self.type == 'Квадрат':
            print(f'Подтип: {self.polygon_sqare}, Количество углов: 4, Способ нахождения площади: S = {self.sq_sqare}\n')
        elif self.type == "Прямоугольник":
            print(f'Подтип: {self.polygon_rectangle}, Количество углов: 4, Способ нахождения площади: S = {self.sq_rectangle}\n')
        elif self.type == "Ромб":
            print(f'Подтип: {self.polygon_romb}, Количество углов: 4, Способ нахождения площади: S = {self.sq_romb}\n')

squar = quadrilateral('Геометрическая фигура', 'Белый', 'Квадрат')
rect = quadrilateral('Геометрическая фигура', 'Красный', 'Прямоугольник')
ro = quadrilateral('Геометрическая фигура', 'Синий', 'Ромб')

squar.info()
squar.extra_info()
rect.info()
rect.extra_info()
ro.info()
ro.extra_info()

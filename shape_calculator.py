class Rectangle():
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return 'Rectangle(width={:d}, height={:d})'.format(self.width, self.height)


    def set_width(self, width):
        self.width = width


    def set_height(self, height):
        self.height = height


    def get_area(self):
        return self.width * self.height


    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    
    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** 0.5

    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return 'Too big for picture.'
        
        canvas = [['*'] * self.width for i in range(self.height)]

        output = ''
        for i, line in enumerate(canvas):
            output += ''.join(line) + '\n'

        return output
    
    
    def get_amount_inside(self, rectangle):
        # No rotation
        if rectangle.height > self.height or rectangle.width > self.width:
            return 0

        return (self.width // rectangle.width) * (self.height // rectangle.height)


class Square(Rectangle):
    def __init__(self, side):
        self.side = side
        super().__init__(side, side)


    def __str__(self):
        return 'Square(side={:d})'.format(self.side)


    def set_side(self, side):
        self.side = side
        self.width = side
        self.height = side


    def set_width(self, width):
        self.set_side(width)


    def set_height(self, height):
        self.set_side(height)

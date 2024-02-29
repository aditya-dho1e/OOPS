class Student:
    name = 'Zoro'

obj = Student()
print(obj.name)


class OnePiece:
    class_attr = 'set sail !!'
    
    # constructor
    def __init__(self, name):
        self.name = name
        print('constructor called')
        
    #method
    def display(self):
        print(self.name)
    
    @staticmethod
    def nika():
        print('Drums of Liberation')
    
    print('One Piece is Real!')
    
obj = OnePiece('Ryuma')

obj.display()
obj.class_attr
obj.name = 'Joyboy'
obj.display()

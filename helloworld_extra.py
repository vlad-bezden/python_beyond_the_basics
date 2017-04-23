'''Here's a less trivial lab, testing your knowledge of basic Python
object-oriented programming.

(Remember: if a method response has quotes around it, that means the
method returns a string.  If there are no quotes, that means it
printed (i.e., using print()).

>>> fido = Dog("Fido")
>>> fido.description()
'Fido the Dog'
>>> fido.speak()
'Woof!'

>>> fifi = Cat("Fifi")
>>> fifi.description()
'Fifi the Cat'
>>> fifi.speak()
'Meow!'

>>> nemo = Fish("Nemo")
>>> nemo.description()
'Nemo the Fish'
>>> nemo.speak()
''

>>> fifi.emote()
Fifi the Cat says: Meow!
>>> fido.emote()
Fido the Dog says: Woof!
>>> nemo.emote()
Nemo the Fish says:

'''


# Write your code here:
class Pat:
    sound = ''

    def __init__(self, name):
        self.name = name

    def description(self):
        return f'{self.name} the {self.__class__.__name__}'

    def speak(self):
        return self.sound

    def emote(self):
        print(f'{self.description()} says:{" " + self.speak() if self.sound else ""}')


class Dog(Pat):
    sound = 'Woof!'


class Cat(Pat):
    sound = 'Meow!'


class Fish(Pat):
    pass


# Do not edit any code below this line!

if __name__ == '__main__':
    import doctest
    doctest.testmod()

# Copyright 2015-2017 Aaron Maxwell. All rights reserved.

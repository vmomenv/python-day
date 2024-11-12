def make_quack(duck):
    duck.quack()

#我们希望传入一个quack方法

class Duck:
    def quack(self):
        print("QUACK!")

class Person:
    def quack(self):
        print("GA!GA!")

real_duck =Duck()
fake_duck =Person()

make_quack(real_duck)
make_quack(fake_duck)

#########
#“如果看起来像鸭子，叫声像鸭子，行为像鸭子，那么它就是鸭子。
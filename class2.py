import class1
class class2:
    def call(self):
        print("inside caller")
        class1.output(self)
self.call()
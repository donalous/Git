class Calculator():
    def init(self,a,b):
        self.a=a
        self.b=b
    def add(self):
        return  self.a + self.b

    def sub(self):
        return self.a-self.b

    def mul(self):
        return self.a*self.b

    def div(self):
        try:
            result = self.a / self.b
        except ZeroDivisionError:
            result = "Ділення на нуль неможливе"
        return result

    def exp(self):
        return  self.a ** self.b

calc = Calculator(4, 0)
print(calc.div())
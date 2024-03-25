class Calculator():
    def __init__(self,a,b):
        self.a=a
        self.b=b
    def exp(self):
        return  self.a ** self.b
    def gcd(self):
        x, y = abs(self.a), abs(self.b)
        while y != 0:
            x, y = y, x % y
        return x
    def lcm(self):
        if self.a == 0 or self.b == 0:
            return 0
        return abs(self.a * self.b) // self.gcd()

print (5)
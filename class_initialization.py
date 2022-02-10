class Fizz:
    foo = {}
    bar = 42


obj1 = Fizz()
obj1.foo["abc"] = 123
obj1.bar += 1
obj2 = Fizz()

# What is the output of these two calls to print?
print(obj2.foo["abc"])
print(obj2.bar)


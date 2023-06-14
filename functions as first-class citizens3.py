def create_adder(x):
    print("x",x)
    def adder(y):
        print("y",y)
        return x-y
    return adder
add_15=create_adder(15)
print(add_15(5))

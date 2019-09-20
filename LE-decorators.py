# Decorators: 9/4/2019

def interior_decorator(func):
    def add_curtains():
        func()
        print("now my house has purple curtains")

    return add_curtains

# def move_in():
    # print("My house was empty, but...")

# Bind returned function from interieor_decorator
# to new varialbe
# new_house = interior_decorator(move_in)
# new_house()

def landscaper(func):
    def add_trees():
        func()
        print("And I planted 12 maples for shade.")
    return add_trees

@landscaper
@interior_decorator
def move_in():
    print("My house was empty, but...")

move_in()

# Passing Args to Internal function

# Decorators: 9/4/2019

def interior_decorator(func):
    def add_curtains(color):
        if color =="orange":
            color = "ugly-ass"
        func(color)
        print(f"now my house has {color} curtains")

    return add_curtains

@interior_decorator
def move_in(color):
    print("My house was empty, but...")

move_in("orange")
move_in("brown")
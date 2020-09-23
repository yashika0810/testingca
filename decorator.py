def decorator(func1):
    def inner():
        print("This is my extra functionality")
        x=int(input("enter value of x"))
        y=int(input("enter value of y"))
        result=x*y
        print(result)
        func1()
    return inner()

@decorator
def need():
    print("Hello I need to be decorated")

need()


# def deco(func):

    def auth():
        #permissions to admin, user
        #username,password=matched

        return func
    return auth



@deco
def login():
    username=field
    email=emailfield
    password=cecxdcw
    






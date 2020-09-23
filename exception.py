while True:
    try:

        x=int(input("enter value of x"))
        y=int(input("enter value of y"))
        avg=(z+y)/2
    
    except ValueError:
        print("Please provide value")

    except NameError:
        print("Please provide coorect value")
 
    finally:
        print("execute everytime")


# def even(l):
#     list1=[]
#     for i in l:
#         if i%2==0:
#             list1.append(i)
#     print(list2)
# print(even([1,2,3,4,5,6,7]))
 

#diff return and print
#make a dunction to reverse a string ( DO NOT USE SLICING AND REVERSE ) [::-1]



# items=[1,2,3,4,5,6]
# sqaure=[]
# for i in items:
#     sqaure.append(i**2)

# print(sqaure)

# map(function,seq)



while True:
    try:
        x=int(input("Enter value of x"))
        y=int(input("Enter value of y"))
        avg=(x+y)/2
        print(avg)
       
        break
    except Exception as e:
        print("Please provide correct")
        print(e)

    finally:
        print("always executes")

    print("random")

   


    
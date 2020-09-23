


# # with argument with return type
# def add(x,y):  #--> function definition --> Formal parameters 
#     # x=10
#     # y=30
#     result=x+y
#     return result

# print(add(40,50) ) # --> function calling --> Actual parameters


# #without argument with return type
# def add():
#     print("Second type")
#     a=int(input("enter value of a"))
#     b=int(input("enter value of b"))
#     return a*b
# x=add()
# print(x)


# #with argument with no return
# def add():

#     print("third type")
#      a=int(input("enter value of a"))
#      b=int(input("enter value of b"))
#     print(a+b)

# x=add()
# print(x)





def even(l):  #defining function 
    list1=[]
    for i in l:
        if i%2==0:
            list1.append(i)
    return list1
print(even([1,2,3,4,5,6,7,8])) #function calling


#reverse --> reverse, [::-1]

# def reverse(str1):
#     new=''
#     index=len(str1) #consultadd --> 10
#     while index>0:
#         new += str1[index-1] #--> str1[9]--> d --> d-->a-->t
#         index=index-1 #-->9
#     return new
# print(reverse("consultadd"))


s="My name is Yashika"
a=s.split()
newlist=[]

for i in a:
   
     if len(i)%2==0:
         newlist.append(i)
print(" ".join(newlist))




# 
# training=["Java", "Python", "aws"]
# print("My trainings are:")
# print("".join(training))


# s="My name is Yashika"
#yM eman si akihsaY"

# a=s.split()
# print(a)





    


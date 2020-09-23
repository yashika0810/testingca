# numbers=[1,2,3,5,7,8,9]
# newlist=[]
# # for i in numbers:
# #     if i%2==0:
# #         newlist.append(i)
# # print(newlist)


# for i in numbers:
#     i=i**2
#     newlist.append(i)
# print(newlist)

# var=[i**2 for i in numbers]
# print(var)


# var=[i for i in range(1,20) if i%2==0 if i>10]
# print(var)
# #Can we have logical operators in list comp?
# #can we have 2 if's and 1 else

# newvar=[i**2 if i%2==0 else i**3 for i in range(1,10)]
# print(newvar)

# mylist=[]
# for i in [20,40,60]:
#     for j in [2,4,6]:
#         mylist.append(i*j)
# print(mylist)

        
# var2=[x*y for x in [20,40,60] for y in [2,4,6]]
# print(var2)


# string1="Hello1235consultadd"
# #s="Helloconsultadd"

# var3=[i for i in string1 if i.isdigit()]
# print(",".join(var3))


#string2=consultadd--> cnsltdd
def get_vowels(string2):
    return [i for i in string2 if i not in 'aieou']

a=get_vowels("consultadd")
print("".join(a))


def palindrome(a):
    return a==a[::-1]
print(palindrome('mom'))
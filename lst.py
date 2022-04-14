import sys 

def lstdet(lst):

    #values will be affected besed on 32 bit or 64 bit os.
    # 64 bit -- 64,8
    # 32 bit -- 36,4
    print("\ncapacity: ",(sys.getsizeof(lst)-64)//8) #sys.getsizeof give memory size

    print("\nsize: ",len(lst))

    print("\nspace left:", ((sys.getsizeof(lst)-64) - len(lst*8))//8)



lst1=[]
print("\n The details of list: ")

lstdet(lst1)
lst1.append("hello")
print("\n adding 1 element:")
lstdet(lst1)
#append
lst1.append("hi")
lst1.append("bye")
lst1.append("See ya")
print(lst1)
lstdet(lst1)

#insert
lst1.insert(1,"new")
print(lst1)
lstdet(lst1)

#delete
lst1.pop(4)
print(lst1)
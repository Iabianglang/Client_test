l=[]

def clear_queue():
    l=[]


def insert_to_the_queue(no):
    if no.isnumeric()== True:
        no=int(no)
        l.insert(0,no)
        # print(l)
        return True

    elif isfloat(no):
        no=float(no)
        l.insert(0,no)
        # print(l)
        return True

    else:
        l.insert(0,no)
        # print(l)
        return True
        

def extract_from_the_queue():
    if len(l)==0:
        return None
        # print("cannot pop from an empty list")
    else:
        a=l.pop()
        return a
        # print(f"object being popped out:{a} ")
        # print(l)


def isfloat(no):
    if no.count('.')==1:
        split=no.split('.')
        if split[0].isnumeric() and split[1].isnumeric():
            return True
        else:
            return False
    
    else:
        return False
    

# while True:
#     enter=input("if you want to insert enter i else enter e for extract:")
#     if enter.startswith("i"):
#         no=input("enter a object:")
#         insert_to_the_queue(no)

#     if enter.startswith("e"):
#         extract_from_the_queue()
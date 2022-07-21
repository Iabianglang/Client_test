# list=[1,1,5,7,9,12,15,15]
# search_no=input("enter the search no: ")

# search_no=int(search_no)

def binary_search(list,search_no):
    if len(list)==0:
        return False

    split_list=len(list)//2
    if list[split_list]==search_no:
        return True

    if list[split_list]>search_no:
        return binary_search(list[:split_list],search_no)

    else:
        return binary_search(list[split_list+1:],search_no)



result=binary_search([1,3,4,5,7],3)

print(f"""index :{result}
value :{list[result]}""")


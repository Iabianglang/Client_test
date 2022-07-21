# coding: utf-8
# a=[1,2,3,4,5.5]
def count(a):
    h={}
    for i in a:
        if i in h:
            h[i]=h[i]+1
        else:
            h[i]=1
    return h

# count([1,2,3,4,5,5,1,5,6])

def fact(y,x):
    if y==0:
        print (x)
        return
    else:
        
        fact(y-1,x*y)
        
Inumber = int(input())
fact(Inumber,Inumber)






    

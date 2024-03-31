def main():
    list1=list(map(int,input('enter the list elements').split()))
    print(list1)
    print("the min element is ; ",minimum(list1))
def minimum(a):
    min=a[0]
    for i in range(1,len(a)):
        
        if min>a[i]:
          min= a[i]
    return min          
main()
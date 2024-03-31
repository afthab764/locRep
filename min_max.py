def main():
    list1=list(map(int,input('enter the list elements').split()))
    print(list1)
    print("the max element is ; ",maximum(list1))
def maximum(a):
    max=a[0]
    for i in range(1,len(a)):
        
        if max<a[i]:
          max= a[i]
    return max          
main()
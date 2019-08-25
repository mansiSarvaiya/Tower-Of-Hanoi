def TowerOfHanoi(n,src,dest,aux):
    if n==1:
        print("Move disk 1 from src ",src,"to dest",dest)
        return
    TowerOfHanoi(n-1,src,aux,dest)
    print("Move disk",n,"from src",src,"to aux",dest)
    TowerOfHanoi(n-1,aux,dest,src)
n=int(input("Enter no of disks"))
if(n>0):
    TowerOfHanoi(n,'A','C','B')

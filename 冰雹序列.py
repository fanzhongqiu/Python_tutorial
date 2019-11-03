print("please input a number:")
pos=eval(input())while pos!=1:
    if pos%2==0:
        pos=pos/2
        print(pos)
        elif pos%2==1:
        pos=pos*3+1
        print(pos)
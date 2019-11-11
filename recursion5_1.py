def pattern(i):
    if i>0:
        print("*",end="");
        i=i-1;
        pattern(i);    

def main():
    i=int(5);

    pattern(i);

if __name__=="__main__":
    main();

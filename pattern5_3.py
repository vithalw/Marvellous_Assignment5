def pattern(i):
    if(i>0):
        print(i,end="");
        i=i-1;
        pattern(i);

def main():
    i=int(input("Enter a value: "));
    pattern(i);
if __name__=="__main__":
    main();
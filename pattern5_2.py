j=int(1);

def pattern(i):
    global j;
    if(j<=i):
        print(j,end="");
        j=j+1;
        pattern(i);


def main():
    i=int(input("Enter any number: "));
    pattern(i);


if __name__=="__main__":
    main();

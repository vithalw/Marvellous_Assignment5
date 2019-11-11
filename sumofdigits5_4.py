result=int(0);
def sum(i):
    global result;
    if(i>0):
        remainder=int(i%10);
        result=result+remainder;
        sum(i/10);
    return result;    

def main():
    i=int(input("Enter a value: "));
    print("Result is: ",sum(i));
if __name__=="__main__":
    main();
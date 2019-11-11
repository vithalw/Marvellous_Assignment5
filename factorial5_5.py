result=int(1);
def factorial(i):
    global result;
    if(i>1):
        result=result*i;
        i=i-1;
        factorial(i);
    return result;    

def main():
    i=int(input("Enter a value: "));
    print("Result is: ",factorial(i));
if __name__=="__main__":
    main();
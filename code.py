# --------------
#Code starts here
def palindrome(num):
    x = [str(y) for y in str(num)]
    l = len(x)
    if l%2 == 0:
        for p in range(int(l/2)):
            
            if x[p]==x[(l-1)-p]:
                pass

            else:
                q=x[(l-1)-p]
                x[(l-1)-p]=x[p]
                if int(''.join(x))<num:
                    x[(l-1)-p]=q
                    x[p]=q

    else:
        x[int(l/2)]=str(int(x[int(l/2)])+1)
        for p in range(int(l/2)):
            
            
            if x[p]==x[(l-1)-p]:
                pass

            else:
                x[(l-1)-p]=x[p]

    return(int(''.join(x)))     

a = palindrome(123)    
print(a)      



# --------------
#Code starts here
def a_scramble(str_1,str_2):
    x= str_1
    y= str_2
    x=x.lower()
    y=y.lower()
    a=[i for i in x]
    b=[i for i in y]
    flag=1
    for i in b:
        if(i in a):
            a.remove(i)
        elif(i not in a):
            flag=0
    if(flag==1):
        return True
    else:
        return False


# --------------
#Code starts here
def check_fib(num):
    a=0;
    b=1;
    sum=0;
    flag=0
    result=[0,1]
    for i in range(1,20):
        sum=a+b;
        a=b;
        b=sum;
        result.append(sum)
    for i in result:
        if(num==i):
            flag=1
    if(flag==1):
        return True 
    else:
        return False



# --------------
#Code starts here
def compress(word):
    word = word.lower()
    res = ""
    ch = word[0]
    num = 1
    index = 0
    while index<len(word)-1:
        if ch==word[index+1]:
            num += 1
            index += 1
        else:
            res += ch+str(num)
            index += 1
            ch = word[index]
            num = 1
    res += ch+str(num)
    return res

ocu=compress("xxcccdex")
print(ocu)


# --------------
#Code starts here
def k_distinct(string,k):
    return len(set(string.lower()))==k

out = k_distinct("Messoptamia",8)
print(out)



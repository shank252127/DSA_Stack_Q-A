#Check for Palindrome

def checkPanildrome(val):
    j=len(val)-1;
    i=0;
    while i<j and val[i]==val[j]:
        j-=1;
        i+=1;
    if(i!=j):
        print("Not Palindrome");
    else:
        print("palindrome");
        
checkPanildrome('madam')
    int sum=0;
    int n=N;
    while(n>0)
    {
        sum+=n%2;
        n=n/2;
    }
    string binary = "";
    while(sum>0)
    {
        if(sum%2==1)
            binary = "1" + binary;
        else
            binary = "0" + binary;
        sum=sum/2;
    }
    return binary;
} 

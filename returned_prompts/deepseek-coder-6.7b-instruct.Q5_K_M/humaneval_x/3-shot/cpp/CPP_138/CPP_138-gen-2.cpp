    int sum=0;
    int count=0;
    for(int i=2;i<n;i+=2){
        if(sum+i>n)
        break;
        sum+=i;
        count++;
    }
    return (sum==n && count==4);
}


A: 
    int sum=0;
    int count=0;
    for(int i=2;i<n;i+=2){
        if(sum+i>n)
        break;
        sum+=i;
        count++;
    }
    return (sum==n && count==4);
}



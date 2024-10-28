    string result;
    int digit;
    int i;
    int length=1;
    int temp=x;
    while (temp/10!=0)
    {
        length+=1;
        temp/=10;
    }
    if (shift>=length){
        temp=x;
        for (i=0;i<length;i++)
        {
            result+=temp%10;
            temp/=10;
        }
        result=result[length-1]+result;
        return result;
    }
    for (i=0;i<shift;i++)
    {
        digit=x%10;
        x/=10;
        x+=digit*pow(10,length-1);
    }
    temp=x;
    for (i=0;i<length-shift;i++)
    {
        result+=temp%10;
        temp/=10;
    }
    return result;
}



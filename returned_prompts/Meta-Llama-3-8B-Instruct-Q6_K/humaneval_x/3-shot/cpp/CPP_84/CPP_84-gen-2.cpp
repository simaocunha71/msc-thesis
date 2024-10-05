    int sum=0;
    int temp=N;
    while (temp>0)
    {
        sum+=temp%2;
        temp/=2;
    }
    string res="";
    while (sum>0)
    {
        if (sum%2==1)
            res="1"+res;
        else
            res="0"+res;
        sum/=2;
    }
    return res;
}

    vector<int> count(2,0);
    int digit;
    num=abs(num);
    while  (num>0)
    {
        digit=num%10;
        if  (digit%2==0)
        count[0]+=1;
        else
        count[1]+=1;
        num/=10;
    }
    return count;
}


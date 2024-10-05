    vector<int> res;
    res.resize(2);
    int i;
    for (i=1;i<=n;i++)
    {
        if (is_palindrome(i))
        {
            res[i%2]+=1;
        }
    }
    return res;
}


bool is_palindrome(int num){
    char chr;
    int i;
    int l=0;
    int r=num;
    while (num>0){
        chr=(num%10)+'0';
        l=r-chr;
        if (l==chr)
        num/=10;
        else
        return false;
    }
    return true;
}





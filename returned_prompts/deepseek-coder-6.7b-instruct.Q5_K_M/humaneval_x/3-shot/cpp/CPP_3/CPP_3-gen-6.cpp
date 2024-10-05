    int balance=0;
    for(auto i:operations)
    {
        balance+=i;
        if(balance<0)
        return true;
    }
    return false;
}



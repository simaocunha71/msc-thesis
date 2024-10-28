    int sum1=0, sum2=0;
    for(auto& i: lst1)
        sum1 += i.size();
    for(auto& i: lst2)
        sum2 += i.size();
    return (sum1<sum2)? lst1 : lst2;
}


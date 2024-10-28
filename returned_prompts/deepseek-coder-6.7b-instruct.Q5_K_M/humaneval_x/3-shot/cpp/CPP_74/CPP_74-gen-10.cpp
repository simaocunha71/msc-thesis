    int sum1=0;
    int sum2=0;
    for(auto &i: lst1)
        sum1+=i.size();
    for(auto &i: lst2)
        sum2+=i.size();
    if(sum1<sum2)
        return lst1;
    else
        return lst2;
}



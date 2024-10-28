    int sum1=0,sum2=0;
    for(auto &str: lst1) sum1+=str.size();
    for(auto &str: lst2) sum2+=str.size();
    return sum1<sum2?lst1:lst2;
}



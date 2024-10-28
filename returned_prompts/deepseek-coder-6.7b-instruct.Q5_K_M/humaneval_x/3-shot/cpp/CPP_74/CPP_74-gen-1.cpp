    int total1 = 0, total2 = 0;
    for(auto &i : lst1) total1 += i.size();
    for(auto &i : lst2) total2 += i.size();
    
    return total1 < total2 ? lst1 : lst2;
}



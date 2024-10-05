    if(n>m)
    return "-1";
    int avg=(n+m)/2;
    if((n+m)%2==1)
    avg++;
    return bitset<32>(avg).to_string();
}



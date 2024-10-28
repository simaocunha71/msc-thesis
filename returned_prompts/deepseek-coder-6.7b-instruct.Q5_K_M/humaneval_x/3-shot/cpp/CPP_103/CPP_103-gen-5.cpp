    if(n>m)
        return "-1";
    int avg=(n+m)/2;
    return bitset<32>(avg).to_string();
}


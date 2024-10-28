    if (n>m)
    return "-1";
    int avg=round((n+m)/2.0);
    string bin_str=bitset<8>(avg).to_string();
    if (bin_str.length()<8)
    bin_str="0"+bin_str;
    return bin_str;
}




    int average;
    if (m<n)
    return "-1";
    average=(n+m)/2;
    return bitset<8>(round(average/2.0)).to_string();
}



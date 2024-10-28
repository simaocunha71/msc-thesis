    if (n>m)
    {
        return "-1";
    }
    int average=(n+m)/2;
    int binary_average=round(average);
    string binary_str="";
    while (binary_average!=0)
    {
        binary_str+=char(binary_average%2+'0');
        binary_average/=2;
    }
    while (binary_str.length()!=n-m)
    {
        binary_str='0'+binary_str;
    }
    return binary_str;
}



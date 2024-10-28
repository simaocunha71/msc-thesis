    int count=0;
    string all_hex_digits="0123456789ABCDEF";
    for (int i=0;i<num.length();i++)
    {
        if (find(all_hex_digits.begin(),all_hex_digits.end(),num[i])!=all_hex_digits.end())
        {
            if (num[i]=='2' || num[i]=='3' || num[i]=='5' || num[i]=='7' || num[i]=='B')
            count+=1;
        }
    }
    return count;
}



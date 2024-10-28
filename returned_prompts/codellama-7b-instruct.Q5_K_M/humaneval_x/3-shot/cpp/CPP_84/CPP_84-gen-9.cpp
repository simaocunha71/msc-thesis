    string binary_string;
    string digits;
    int i;
    if (N==0)
    return "0";
    else
    {
        while (N>0)
        {
            digits.push_back(N%2+'0');
            N/=2;
        }
        int j=0;
        int k=digits.length()-1;
        while (j<k)
        {
            binary_string.push_back(digits[j]+digits[k]);
            j+=1;
            k-=1;
        }
        return binary_string;
    }
}



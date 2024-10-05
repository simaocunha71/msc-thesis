    vector<int> digits;
    int i;
    for (i=0;i<3;i++)
        digits.push_back(number%10);
    digits[1]+=digits[2]*10;
    digits.pop_back();
    digits[0]+=digits[1]*10;
    digits.pop_back();
    digits[0]+=digits[1]*10;
    digits.pop_back();
    string result="";
    for (i=0;i<3;i++)
    {
        if (digits[i]==1) result+="i";
        if (digits[i]==2) result+="ii";
        if (digits[i]==3) result+="iii";
        if (digits[i]==4) result+="iv";
        if (digits[i]==5) result+="v";
        if (digits[i]==6) result+="vi";
        if (digits[i]==7) result+="vii";
        if (digits[i]==8) result+="viii";
        if (digits[i]==9) result+="ix";
    }
    return result;
}


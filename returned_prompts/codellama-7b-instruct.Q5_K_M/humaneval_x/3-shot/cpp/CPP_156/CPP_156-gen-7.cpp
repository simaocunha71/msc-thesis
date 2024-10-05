    vector<string> romans {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    vector<int> vals {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman_str;
    int i;
    for (i=0;i<vals.size();i++)
    {
        while (number>=vals[i])
        {
            number-=vals[i];
            roman_str+=romans[i];
        }
    }
    return roman_str;
}


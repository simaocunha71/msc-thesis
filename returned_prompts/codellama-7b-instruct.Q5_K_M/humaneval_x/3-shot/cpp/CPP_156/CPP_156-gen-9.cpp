    vector<string> roman_num_str;
    roman_num_str.push_back("M");
    roman_num_str.push_back("CM");
    roman_num_str.push_back("D");
    roman_num_str.push_back("CD");
    roman_num_str.push_back("C");
    roman_num_str.push_back("XC");
    roman_num_str.push_back("L");
    roman_num_str.push_back("XL");
    roman_num_str.push_back("X");
    roman_num_str.push_back("IX");
    roman_num_str.push_back("V");
    roman_num_str.push_back("IV");
    roman_num_str.push_back("I");
    
    int i;
    string roman_num;
    for (i=0;i<13;i++)
    {
        while (number>=roman_num_str[i].length())
        {
        roman_num+=roman_num_str[i];
        number-=roman_num_str[i].length();
        }
    }
    return roman_num;
}



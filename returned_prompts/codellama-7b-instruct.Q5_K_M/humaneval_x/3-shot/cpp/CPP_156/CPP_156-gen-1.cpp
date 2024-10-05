    string roman_number;
    vector<string> roman_digits;
    roman_digits.push_back("i");
    roman_digits.push_back("v");
    roman_digits.push_back("x");
    roman_digits.push_back("l");
    roman_digits.push_back("c");
    roman_digits.push_back("d");
    roman_digits.push_back("m");
    
    int i;
    int digit_value;
    int sub_number=number;
    for (i=0;i<sub_number;i++)
    {
        digit_value=sub_number%10;
        if (digit_value==9)
        roman_number+=roman_digits[i];
        else if (digit_value==4)
        roman_number+=roman_digits[i]+roman_digits[i+1];
        else if (digit_value==5)
        roman_number+=roman_digits[i+1];
        else if (digit_value==4)
        roman_number+=roman_digits[i]+roman_digits[i+1];
        else if (digit_value==9)
        roman_number+=roman_digits[i];
        else if (digit_value==4)
        roman_number+=roman_digits[i]+roman_digits[i+1];
        else if (digit_value==5)
        roman_number+=roman_digits[i+1];
        else if (digit_value==4)
        roman_number+=roman_digits[i]+roman_digits[i+1];
        else if (digit_value==9)
        roman_number+=roman_digits[i];
        else if (digit_value==4)
        roman_number+=roman_digits[i]+roman_digits[i+1];
        else if (digit_value==5)
        roman_number+=roman_digits[i+1];
        else if (digit_value==4)
        roman_number+=roman
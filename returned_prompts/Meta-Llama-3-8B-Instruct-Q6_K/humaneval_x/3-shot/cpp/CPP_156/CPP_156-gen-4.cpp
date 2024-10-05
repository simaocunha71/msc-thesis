    vector<string> roman_map = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    vector<int> roman_values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string roman;
    int i;
    for (i=0;i<roman_values.size();i++)
    {
        while (number>=roman_values[i])
        {
            roman += roman_map[i];
            number -= roman_values[i];
        }
    }
    return roman;
} // end function int_to_mini_roman


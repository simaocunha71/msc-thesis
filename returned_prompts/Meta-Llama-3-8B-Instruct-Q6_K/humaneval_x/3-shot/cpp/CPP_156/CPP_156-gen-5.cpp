    vector<string> romans={ "M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I" };
    vector<int> values={ 1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1 };
    string result = "";
    int i;
    for (i=0;i<values.size();i++)
    {
        while(number>=values[i])
        {
            number -= values[i];
            result += romans[i];
        }
    }
    return result;
}
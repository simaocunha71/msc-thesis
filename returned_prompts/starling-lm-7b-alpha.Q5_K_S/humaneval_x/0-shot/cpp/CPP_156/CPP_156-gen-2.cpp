    vector<string> v = {
        "i", "ii", "iii",
        "iv", "v", "vi", "vii", "viii", "ix",
        "x", "xl", "xx", "xxl", "xxx", "xl",
        "c", "xc", "xc", "xc", "cd", "c",
        "d", "dc", "dcc", "dccc", "cm",
        "m"};
    return v[number - 1];
}


/*
Given a string, return its roman numeral equivalent as an integer.
Restrictions: 0 <= len <= 15, len only contains the characters 'i', 'v', and 'x'.

Examples:
>>> roman_to_mini_int("i") == 1
>>> roman_to_mini_int("ii") == 2
>>> roman_to_mini_int("iv") == 4
>>> roman_to_mini_int("v") == 5
>>> roman_to_mini_int("vi") == 6
>>> roman_to_mini_int("vii") == 7
>>> roman_to_mini_int("viii") == 8
>>> roman_to_mini_int("ix") == 9
>>> roman_to_mini_int("x") == 10
>>> roman_to_mini_int("xl") == 40
>>> roman_to_mini_int("xc") == 90
>>> roman_to_mini_int("cd") == 400
>>> roman_to_mini_int("cm") == 900
*/
int roman_to_mini_int(string s){
    int n = s.length();
    int i = 0;
    int res = 0;
    while(i < n){
        if(s[i] == 'i') res += 1;
        else if(s[i] == 'v') res += 5;
        else if(s[i] == 'x') res += 10;
        i++;
    }
    return res;
}




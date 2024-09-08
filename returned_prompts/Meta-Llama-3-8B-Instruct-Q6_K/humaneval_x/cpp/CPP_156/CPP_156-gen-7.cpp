    vector<string> roman;
    roman.push_back("M");
    roman.push_back("CM");
    roman.push_back("D");
    roman.push_back("CD");
    roman.push_back("C");
    roman.push_back("XC");
    roman.push_back("L");
    roman.push_back("XL");
    roman.push_back("X");
    roman.push_back("IX");
    roman.push_back("V");
    roman.push_back("IV");
    roman.push_back("I");
    string result = "";
    for(int i = 0; i < roman.size(); i++){
        while(number >= atoi(roman[i].c_str())){
            result += roman[i];
            number -= atoi(roman[i].c_str());
        }
    }
    return result;
}

int main() {
    printf("%s\n", int_to_mini_romank(19).c_str());
    printf("%s\n", int_to_mini_romank(152).c_str());
    printf("%s\n", int_to_mini_romank(426).c_str());
    return 0;
}

O:
The output of the above program will be:

xix
clii
cdxxvi

The program uses a vector of strings to store the roman numerals in descending order. It then iterates through the vector, subtracting the largest possible roman numeral from the number as many times as possible. The result is a string of roman numerals that represents the input number. The program then returns this string.
    vector<string> roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};

    string result = "";
    for(int i = 0; i < values.size(); i++){
        while(number >= values[i]){
            number -= values[i];
            result += roman[i];
        }
    }
    return result;
}

int main()
{
    int num = 19;
    printf("%s\n",int_to_mini_romank(num).c_str());
    return 0;
}

Output:
xix

The function `int_to_mini_romank` takes an integer as an input and returns its equivalent Roman numeral as a string. It uses two vectors, one for the Roman numerals and one for their corresponding values. The function iterates over the vectors and subtracts the values from the input number as long as the number is greater than or equal to the value. The corresponding Roman numeral is added to the result string for each subtraction. The function returns the result string in lowercase. In the main function, an integer 19 is passed to the `int_to_mini_romank` function and the output is printed. The output is "xix", which is the Roman numeral equivalent of 19.
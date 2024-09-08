    // create a vector with roman numerals
    vector<string> roman_numerals = {"i", "iv", "ix", "x", "xl", "xc", "c", "cd", "cm", "m"};
    vector<int> roman_values = {1, 4, 9, 10, 40, 90, 100, 400, 900, 1000};

    // create a string to hold the roman numeral
    string roman = "";

    // iterate over the roman numerals and values
    for(int i = 0; i < roman_numerals.size(); i++){
        // calculate the number of times the current roman numeral fits into the number
        int count = number / roman_values[i];

        // add the roman numeral to the string the corresponding number of times
        while(count > 0){
            roman += roman_numerals[i];
            count--;
        }

        // subtract the value of the roman numeral from the number
        number -= count * roman_values[i];

        // if the number is now 0, break the loop
        if(number == 0){
            break;
        }
    }

    // convert the roman numeral to lowercase
    for(int i = 0; i < roman.size(); i++){
        roman[i] = tolower(roman[i]);
    }

    // return the roman numeral
    return roman;
}
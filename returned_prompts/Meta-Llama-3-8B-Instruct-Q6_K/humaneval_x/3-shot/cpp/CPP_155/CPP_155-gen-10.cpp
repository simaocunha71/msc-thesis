    vector<int> result(2, 0);
    string str = to_string(abs(num));
    for (int i = 0; i < str.length(); i++) {
        if (str[i] % 2 == 0) {
            result[0]++;
        } else {
            result[1]++;
        }
    }
    return result;
}  // Return a vector with even and odd counts
// The even count is the first element and the odd count is the second
// For example, even_odd_count(123) returns {1, 2} because 1 is odd and 2 is even
// We use the absolute value of the number to handle negative numbers
// We convert the number to a string to easily iterate over each digit
// For each digit, we check if it is even or odd using the modulus operator
// We increment the corresponding count in the result vector
// Finally, we return the result vector
}  // end of function even_odd_count
//  Return a vector that has the number of even and odd digits respectively
//  Example: even_odd_count(-12) returns {1, 1} because -12 has 1 even and 1 odd digit
//  even_odd_count(123) returns {1, 2} because 123 has 1 even and 2 odd digits
//  even_odd_count(0) returns {1, 0} because 0 has 1 even digit and 0 odd digits
//  even_odd_count(999) returns {0, 3} because 999 has 0 even digits and 3 odd digits
//  even_odd_count(-999) returns {0, 3} because -999 has 0 even digits and 3 odd digits
//  even_odd_count(0.5) will not work as this function is designed to work with integers
//  We use the modulus operator to check if a number is even or odd
//  The modulus operator returns the remainder of the division of its two arguments
//  If the remainder is 0, then the number is even, otherwise it is odd
//  We convert the number to a string to easily iterate over each digit
//  For each digit, we check if it is even or odd using the modulus operator
//  We increment the corresponding count in the result vector
//  Finally, we return the result vector
}  // end of function even_odd_count
// 
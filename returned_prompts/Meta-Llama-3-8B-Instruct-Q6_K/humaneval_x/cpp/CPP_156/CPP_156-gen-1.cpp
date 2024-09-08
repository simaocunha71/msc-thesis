    vector<string> roman = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    string result = "";

    for (int i = 0; i < values.size(); i++) {
        while (number >= values[i]) {
            number -= values[i];
            result += roman[i];
        }
    }
    return result;
}

B:
    // Write the code for the function int_to_mini_romank here
    // This function takes an integer as input and returns its roman numeral equivalent as a string in lowercase
    // For example, int_to_mini_roman(19) should return "xix"
    // int_to_mini_roman(152) should return "clii"
    // int_to_mini_roman(426) should return "cdxxvi"

    // Start with the largest possible roman numeral value (1000) and subtract it from the number until it is no longer possible
    // Then, subtract the next largest roman numeral value (900) and add it to the result
    // Continue this process until the number is 0
    // Use the roman numeral values and their corresponding strings to build the result string

    // The following code is a simple implementation of the above idea
    // It is not very efficient, but it works for the given range of numbers
    // You can improve it by using a more efficient algorithm or adding more features

    // Start writing your code here
    string int_to_mini_romank(int number) {
        string roman = "";
        // Start with the largest possible roman numeral value (1000)
        if (number >= 1000) {
            roman += "m";
            number -= 1000;
        }
        // Then, subtract the next largest roman numeral value (900) and add it to the result
        if (number >= 900) {
            roman += "cm";
            number -= 900;
        }
        // Continue this process until the number is 0
        if (number >= 500) {
            roman += "d";
            number -= 500;
        }
        if (number >= 400) {
            roman
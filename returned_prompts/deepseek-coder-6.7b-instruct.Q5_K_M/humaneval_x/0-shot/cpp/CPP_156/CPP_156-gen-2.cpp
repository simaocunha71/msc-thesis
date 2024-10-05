    vector<int> values = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> numerals = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string result = "";

B:
    for(int i = 0; i < values.size(); i++){
        while(number >= values[i]){
            number -= values[i];
            result += numerals[i];
        }
    }

C:
    return result;
}

int main() {
    printf("%s\n", int_to_mini_roman(19).c_str());
    printf("%s\n", int_to_mini_roman(152).c_str());
    printf("%s\n", int_to_mini_roman(426).c_str());
    return 0;
}

The code works by going through each value and numerals pair in turn, starting from the highest. If the current value is less than or equal to the remaining number, it subtracts the value from the number and adds the corresponding numeral to the result. This is done repeatedly until the number is 0, at which point the result is returned.

The time complexity is O(1), as the number of iterations is constant and does not depend on the size of the input. The space complexity is also O(1), as the amount of extra space used does not depend on the size of the input.
*/

// 1.14.2022
// Code by: P.S.M.R
// Edited: P.S.M.R
// Edited: P.S.M.R
// Edited: P.S.M.R
// Edited: P.S.M.R
// Edited: P.S.M.R
// Edited: P.S.M.R
// Edited: P.S.
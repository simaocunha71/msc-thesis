    vector<int> numbers = {1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1};
    vector<string> roman = {"m", "cm", "d", "cd", "c", "xc", "l", "xl", "x", "ix", "v", "iv", "i"};
    string res = "";

B:
    for(int i=0; i<numbers.size(); i++){
        while(number >= numbers[i]){
            res += roman[i];
            number -= numbers[i];
        }
    }

C:
    return res;
}

int main() {
    printf("%s\n", int_to_mini_roman(19).c_str());
    printf("%s\n", int_to_mini_roman(152).c_str());
    printf("%s\n", int_to_mini_roman(426).c_str());
    return 0;
}


A: Initialization:
Start by defining the vectors for the numbers and their corresponding roman numerals.

B:
Iterating through the numbers vector, while the number is greater than or equal to the current number in the vector:

- Add the roman numeral equivalent to the result string.
- Subtract the current number from the number.

C:
Return the result string.


This program works by going through a list of roman numerals from highest to lowest, and subtracting the highest possible value from the number until the number is less than the value. This continues for each value in the list, building the roman numeral equivalent as it goes.

This solution is efficient as it only requires a single pass through the numbers vector for each input, and the while loop only executes a constant number of times for each input. The total time complexity of the solution is O(1), as there is a constant number of operations regardless of the input size.

The space complexity is also O(1), as the space used does not increase with the size of the input.
*/

        int sum = 0;
        for(int i = 0; i < s.length(); i++) {
            char c = s.charAt(i);
            if(Character.isUpperCase(c)) {
                sum += (int) c;
            }
        }
        return sum;
    }
}

Explanation:
The function digitSum takes a string s as input.

It initializes a variable sum to 0 which will hold the sum of ASCII values of uppercase characters.

Then, it loops through each character c in the string s.

If the character c is an uppercase letter (checked using the isUpperCase method of the Character class), its ASCII value is added to sum.

Finally, the function returns the sum of the ASCII values of the uppercase characters.

This solution works by first initializing a variable sum to 0, which will hold the sum of ASCII values of uppercase letters. 

Then, it loops through each character in the input string. If the character is an uppercase letter, its ASCII value is added to sum. 

Finally, the function returns the sum of the ASCII values of the uppercase letters.

This is done by converting the character to its integer ASCII value using the (int) cast, and then adding this value to sum.

If the character is not an uppercase letter, the function simply moves on to the next character. 

The time complexity of this solution is O(n), where n is the length of the input string, because it must examine each character in the string once.

The space complexity is O(1), because it uses a constant amount of space to store the sum and the input string, and does not depend on the size of the input.

The isUpperCase method from the Character class is used to check if the character is an uppercase letter. 

The integer ASCII value of an uppercase letter is added to sum.
    */
}#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

int main() {
    int n;
    cin >> n;
    vector<int> arr(n);
    for (int i = 0; i < n;
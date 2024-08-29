#include <vector>
#include <algorithm>
#include <cmath>
using namespace std;

class Solution {
public:
    vector<int> even_odd_count(int num) {
        vector<int> result(2, 0);
        num = abs(num);
        while (num > 0) {
            int digit = num % 10;
            if (digit % 2 == 0) {
                result[0]++;
            } else {
                result[1]++;
            }
            num /= 10;
        }
        return result;
    }
};

/*
Solution
1. The problem requires counting the number of even and odd digits in a given integer.
2. To solve this problem, we can use a vector to store the count of even and odd digits.
3. We initialize the vector with two elements, both set to 0.
4. We then take the absolute value of the given number to handle negative numbers.
5. We use a while loop to iterate through each digit of the number.
6. In each iteration, we extract the last digit of the number using the modulus operator (%).
7. We check if the digit is even or odd and increment the corresponding count in the vector.
8. We then divide the number by 10 to remove the last digit.
9. Finally, we return the vector containing the counts of even and odd digits.
*/
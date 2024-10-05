    string s = to_string(x);
    int n = s.size();
    if(shift > n) return string(s.rbegin(), s.rend());
    s = s.substr(n-shift, shift) + s.substr(0, n-shift);
    return s;
}

int main() {
    printf("Result: %s\n", circular_shift(12, 1).c_str());
    printf("Result: %s\n", circular_shift(12, 2).c_str());
    return 0;
}

In this solution, the function circular_shift first converts the integer x into a string s. It then checks if the shift is greater than the number of digits in x. If so, it returns the reverse of the string.

If shift is not greater than the number of digits in x, the function performs a circular shift by taking a substring of the last shift digits and appending it to the beginning of the remaining digits in the string. This is done using the substr function and the + operator for string concatenation. The function returns the shifted string.

In the main function, the circular_shift function is called with different inputs and the results are printed to the console.
*/

#include<stdio.h>
#include<string.h>

char* circular_shift(int x, int shift) {
    char buffer[50];
    sprintf(buffer, "%d", x);
    int len = strlen(buffer);
    if (shift > len) {
        for (int i = 0; i < len / 2; i++) {
            char temp = buffer[i];
            buffer[i] = buffer[len - 1 - i];
            buffer[len - 1 - i] = temp;
        }
    } else {
        char temp[50];
        strncpy(temp, buffer + len - shift, shift);
        temp[shift] = '\0';
        strncpy(buffer, buffer, len - shift);
        buffer[len - shift] = '\0';
        strcat(buffer, temp);
    }
    return strdup(buffer);
}


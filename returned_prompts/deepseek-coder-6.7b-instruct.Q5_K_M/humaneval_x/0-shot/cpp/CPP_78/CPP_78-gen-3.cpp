    int count = 0;
    string hex_primes = "2357BDF";
    for(int i = 0; i < num.size(); i++){
        if(hex_primes.find(num[i]) != string::npos) count++;
    }
    return count;
}

int main() {
    string num;
    printf("Enter hexadecimal number: ");
    cin >> num;
    printf("Count of prime hexadecimal digits: %d\n", hex_key(num));
    return 0;
}
*/

*/
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>

int hex_key(std::string num){
    int count = 0;
    std::vector<char> hex_primes = {'2', '3', '5', '7', 'B', 'D', 'F'};
    for(int i = 0; i < num.size(); i++){
        if(std::find(hex_primes.begin(), hex_primes.end(), num[i]) != hex_primes.end()) count++;
    }
    return count;
}

int main() {
    std::string num;
    std::cout << "Enter hexadecimal number: ";
    std::cin >> num;
    std::cout << "Count of prime hexadecimal digits: " << hex_key(num) << std::endl;
    return 0;
}

/*
Explanation:
The program first defines a function called hex_key that takes a string as an argument. This string represents a hexadecimal number.

The function initializes a counter to 0 and a vector of characters representing prime hexadecimal digits. It then iterates through each character in the input string. If the current character is found in the vector of prime hexadecimal digits, it increments the counter.

Finally, the function returns the counter, which represents the number of prime hexadecimal digits in the input string.

In the main function, the program prompts the user to enter a hexadecimal number.
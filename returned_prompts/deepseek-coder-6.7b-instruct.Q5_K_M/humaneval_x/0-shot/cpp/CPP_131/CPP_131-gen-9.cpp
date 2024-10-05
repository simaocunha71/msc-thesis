    int odd_product = 1;
    bool odd_found = false;
    while(n != 0){
        int digit = n % 10;
        if(digit % 2 != 0){
            odd_product *= digit;
            odd_found = true;
        }
        n /= 10;
    }
    return odd_found ? odd_product : 0;
}
*/


int main(){
    int n;
    printf("Enter a number: ");
    scanf("%d",&n);
    printf("%d\n",digits(n));
    return 0;
}

//C++/src/oddDigitProduct/test_oddDigitProduct.cpp
#define CATCH_CONFIG_MAIN  // This tells Catch to provide a main() - only do this in one cpp file
#include "catch.hpp"
#include "oddDigitProduct.cpp"

TEST_CASE("Odd Digit Product"){
    REQUIRE(digits(1) == 1);
    REQUIRE(digits(4) == 0);
    REQUIRE(digits(235) == 15);
    REQUIRE(digits(2468) == 0);
    REQUIRE(digits(13579) == 315);
    REQUIRE(digits(9875) == 75);
}//C++/src/palindrome/palindrome.cpp
#include <iostream>
#include <string>
#include <cctype>

using namespace std;

bool isPalindrome(string str) {
    int start = 0;
    int end = str.size() - 1;

    while (start < end) {
        // ignore non-alphanumeric characters
        if (!isalnum(str[start])) {
            start++;
        } else if (!isalnum(str[end])) {
            end--;
        } else {
            // compare characters case-insensitively
            if (tolower(str[start]) != tolower(str[end])) {
               
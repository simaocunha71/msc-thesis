    int count_odd=0, count_even=0;
    for(int i=1; i<=n; i++){
        string s = to_string(i);
        string r = string(s.rbegin(), s.rend());
        if(s==r){
            if(s.length() % 2 == 0) count_even++;
            else count_odd++;
        }
    }
    return {count_even, count_odd};
}
int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)", res[0], res[1]);
    return 0;
}

*/

// S:
// The question asks us to count the number of even and odd integer palindromes from 1 to n.
// We initialize two counters, count_odd and count_even, to 0. We then loop through all the numbers from 1 to n.
// For each number, we convert it to a string and then reverse it. If the original string is equal to the reversed string, 
// it means that the number is a palindrome. If the length of this palindrome is even, we increment count_even. 
// Otherwise, we increment count_odd. Finally, we return a vector containing count_even and count_odd.
// This solution has a time complexity of O(n*m), where n is the number of numbers from 1 to n and m is the length of the string representation of each number.

// E:
// The problem does not specify a language, but the code is written in C++. The function even_odd_palindrome takes an integer n as input and returns a vector containing the count of even and odd integer palindromes from 1 to n.
// The main function reads an integer from the standard input, calls the function even_odd_palindrome with this input, and then prints the returned vector to the standard output.

// T:
// Test this code with inputs 3 and 12. The output should be (1, 2) and (4, 6), respectively.
// The code works as
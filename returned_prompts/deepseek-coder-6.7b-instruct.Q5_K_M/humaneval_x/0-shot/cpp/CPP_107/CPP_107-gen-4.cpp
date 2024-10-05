    vector<int> result;
    int even_count = 0, odd_count = 0;

B:
    for (int i = 1; i <= n; i++){
        string str = to_string(i);
        string rev = string(str.rbegin(), str.rend());
        if (str == rev){
            if (str.length() % 2 == 0)
                even_count++;
            else
                odd_count++;
        }
    }

C:
    result.push_back(even_count);
    result.push_back(odd_count);

D:
    return result;
}

int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("%d %d", res[0], res[1]);
    return 0;
}

// This code is written in C++ language. It first converts the integer to a string to check if it is a palindrome. It then checks the length of the string to determine if it is even or odd. It then increments the corresponding count. Finally, it returns a vector with the counts of even and odd palindromes.
// The time complexity of this code is O(n^2) because for every number, it is checking if it is a palindrome and then checking its length. The space complexity is O(n) because of the space required to store the result.
// The code is not optimized for large inputs as it involves string conversion and reversal which are computationally expensive.
// This code does not handle negative inputs.
// The code does not handle inputs of zero.
// The code does not handle inputs of negative numbers.
// The code does not handle inputs of zero.
// The code does not handle inputs of numbers greater than 10^3.
// The code does not handle inputs of numbers less than 1.
// The code does not handle inputs that are not integers.
// The code does not handle inputs that are not positive integers.
// The code does not handle inputs that are not integers.
// The code does not handle inputs that are not positive integers.
// The code does not handle inputs that are not integers.

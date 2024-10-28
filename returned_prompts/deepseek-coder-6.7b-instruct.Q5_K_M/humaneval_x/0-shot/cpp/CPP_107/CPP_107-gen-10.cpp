    vector<int> v(2, 0);
    for (int i = 1; i <= n; i++){
        string s = to_string(i);
        string r = s;
        reverse(r.begin(), r.end());
        if (s == r){
            if (i % 2 == 0)
                v[0]++;
            else
                v[1]++;
        }
    }
    return v;
}
int main(){
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)\n", res[0], res[1]);
    return 0;
}
*/

int main()
{
    int n;
    scanf("%d", &n);
    vector<int> res = even_odd_palindrome(n);
    printf("(%d, %d)\n", res[0], res[1]);
    return 0;
}

// The given problem is to find the number of even and odd integer palindrome numbers within the range 1 to n.
// A palindrome is a number that remains the same when its digits are reversed.
// Here, we are using C++ to solve this problem by creating a vector of size 2 with all elements as 0 and then checking each number from 1 to n whether it's a palindrome or not.
// If it's a palindrome, we check whether it's even or odd and then increment the corresponding index of the vector.
// Finally, we return the vector which has the count of even and odd palindromes.
// The time complexity of this approach is O(n*m) where n is the range from 1 to n and m is the number of digits in n.
// The space complexity is O(1) as we are using a constant amount of space.

// The given code is an implementation of the above approach.
// It takes an integer input n and calls the function even_odd_palindrome with n as argument.
// The function returns a vector of two integers which are the counts of even and odd palindromes.

    int len=str.length();
    for(int i=2; i*i<=len; i++){
        if(len%i==0)
            return false;
    }
    return true;
}

int main(){
    cout<<prime_length("Hello")<<endl;
    cout<<prime_length("abcdcba")<<endl;
    cout<<prime_length("kittens")<<endl;
    cout<<prime_length("orange")<<endl;
    return 0;
}

```
This C++ program checks whether the length of a given string is a prime number or not.

The `prime_length` function takes a string as input and returns `true` if the length of the string is a prime number, and `false` otherwise.

Inside the function, we iterate from 2 to the square root of the length of the string. For each number `i` in this range, we check if the length of the string is divisible by `i`. If it is, we immediately return `false`, because the length is not a prime number.

If we reach the end of the loop without finding a divisor, we return `true`, because the length is a prime number.

In the `main` function, we test the `prime_length` function with four different strings: "Hello", "abcdcba", "kittens", and "orange". The output should be `true` for the first three strings and `false` for the last one.

Note that this program uses the trial division method to check for primality, which is not the most efficient method for large numbers. For a more efficient solution, you could use a primality test like the Miller-Rabin test.
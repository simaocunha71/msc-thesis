    int n = str.length();
    if (n <= 1)
        return false;
    if (n <= 3)
        return true;
    if (n % 2 == 0 || n % 3 == 0)
        return false;
    for (int i = 5; i * i <= n; i = i + 6)
        if (n % i == 0 || n % (i + 2) == 0)
            return false;
    return true;
}

int main() {

    string str1 = "Hello";
    if(prime_length(str1)) {
        printf("True\n");
    } else {
        printf("False\n");
    }

    string str2 = "abcdcba";
    if(prime_length(str2)) {
        printf("True\n");
    } else {
        printf("False\n");
    }

    string str3 = "kittens";
    if(prime_length(str3)) {
        printf("True\n");
    } else {
        printf("False\n");
    }

    string str4 = "orange";
    if(prime_length(str4)) {
        printf("True\n");
    } else {
        printf("False\n");
    }

    return 0;
}
*/

/*
prime_length is a function that takes a string as an argument and returns a boolean value. It first gets the length of the string. If the length is less than or equal to 1, it returns false as strings with length less than or equal to 1 are not prime. If the length is less than or equal to 3, it returns true as strings with length 2 or 3 are prime. If the length is divisible by 2 or 3, it returns false as strings with length divisible by 2 or 3 are not prime. Then, it checks if the length is divisible by any number between 5 and the square root of the length. If it is divisible, it returns false as strings with length divisible by any number other than 1 and itself are not prime. If the length is not divisible by any of the numbers, it returns true as the length is prime.

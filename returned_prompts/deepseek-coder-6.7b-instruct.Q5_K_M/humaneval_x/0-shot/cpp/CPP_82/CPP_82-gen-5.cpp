    int length = str.size();
    if (length < 2) return false;
    for (int i = 2; i*i <= length; ++i) {
        if (length % i == 0) return false;
    }
    return true;
}

int main(){
    printf(prime_length("Hello")? "true" : "false");
    printf(prime_length("abcdcba")? "true" : "false");
    printf(prime_length("kittens")? "true" : "false");
    printf(prime_length("orange")? "true" : "false");
    return 0;
}


A: The function prime_length is checking whether the length of the string is a prime number or not.


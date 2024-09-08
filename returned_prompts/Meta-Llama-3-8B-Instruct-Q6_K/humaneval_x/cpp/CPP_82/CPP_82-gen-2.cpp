    int len = str.length();
    bool isPrime = true;
    for(int i = 2; i*i <= len; i++){
        if(len % i == 0){
            isPrime = false;
            break;
        }
    }
    return isPrime;
}

int main() {
    string s = "Hello";
    printf("%d\n", prime_length(s));
    return 0;
}


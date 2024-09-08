    int product = 1;
    string str = to_string(n);
    for(int i = 0; i < str.length(); i++){
        if((str[i] - '0') % 2 != 0){
            product *= (str[i] - '0');
        }
    }
    return product;
}

B:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

C:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

D:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

E:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

F:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

G:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return product;
}

H:
int digits(int n) {
    int product = 1;
    while(n > 0) {
        int digit = n % 10;
        if(digit % 2 != 0) {
            product *= digit;
        }
        n /= 10;
    }
    return
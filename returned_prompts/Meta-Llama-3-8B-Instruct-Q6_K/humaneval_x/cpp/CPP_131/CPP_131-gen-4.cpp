    string s = to_string(n);
    int product = 1;
    for(int i = 0; i < s.length(); i++){
        int digit = s[i] - '0';
        if(digit % 2 != 0){
            product *= digit;
        }
    }
    return product;
}

B:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n / 10;
        }
        return product;
    }
}C:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n / 10;
        }
        return product;
    }D:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n / 10;
        }
        return product;
    }
}E:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n / 10;
        }
        return product;
    }F:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n / 10;
        }
        return product;
    }G:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n / 10;
        }
        return product;
    }H:
    int digits(int n){
        int product = 1;
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 != 0){
                product *= digit;
            }
            n = n /
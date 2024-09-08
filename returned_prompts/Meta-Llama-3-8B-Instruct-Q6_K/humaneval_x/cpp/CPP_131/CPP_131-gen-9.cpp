    int product = 1;
    string s = to_string(n);
    for(int i = 0; i < s.size(); i++){
        if(s[i] - '0' % 2 == 1){
            product *= (s[i] - '0');
        }
    }
    return product;
}

B:
    int digits(int n) {
        int product = 1;
        while (n) {
            int digit = n % 10;
            if (digit % 2) {
                product *= digit;
            }
            n /= 10;
        }
        return product;
    }

C:
    int digits(int n) {
        int product = 1;
        while (n) {
            n = n / 10;
            if (n % 2) {
                product *= n % 10;
            }
        }
        return product;
    }

D:
    int digits(int n) {
        int product = 1;
        while (n) {
            n = n / 10;
            if ((n % 10) % 2) {
                product *= (n % 10);
            }
        }
        return product;
    }

E:
    int digits(int n) {
        int product = 1;
        while (n) {
            int digit = n % 10;
            if (digit % 2) {
                product *= digit;
            }
            n /= 10;
        }
        return product;
    }

F:
    int digits(int n) {
        int product = 1;
        while (n) {
            n = n / 10;
            if (n % 2) {
                product *= n % 10;
            }
        }
        return product;
    }

G:
    int digits(int n) {
        int product = 1;
        while (n) {
            n = n / 10;
            if ((n % 10) % 2) {
                product *= (n % 10);
            }
        }
        return product;
    }

H:
    int digits(int n) {
        int product = 1;
        int remainder;
        while (n) {
            remainder = n % 10;
            if (remainder % 2) {
                product *= remainder;
            }
            n /= 10;
        }
        return product;
    }

I:
    int digits(int n) {
        int product = 1;
        int remainder;
        while
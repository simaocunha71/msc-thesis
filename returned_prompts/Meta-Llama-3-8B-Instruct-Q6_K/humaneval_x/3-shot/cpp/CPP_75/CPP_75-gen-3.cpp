    for(int i = 2; i <= sqrt(a); i++) {
        if(a%i == 0) {
            int j = i;
            while(a % j == 0) {
                a /= j;
            }
            if(is_prime(j)) {
                if(a == 1) {
                    return true;
                }
            }
        }
    }
    return false;
}

bool is_prime(int x) {
    if(x <= 1) {
        return false;
    }
    for(int i = 2; i <= sqrt(x); i++) {
        if(x % i == 0) {
            return false;
        }
    }
    return true;
} 
// You can also use this solution which is more efficient
bool is_multiply_prime(int a){
    int i = 2;
    while(i*i <= a){
        if(a%i == 0){
            int j = i;
            while(a % j == 0) {
                a /= j;
            }
            if(is_prime(j)) {
                if(a == 1) {
                    return true;
                }
            }
        }
        i++;
    }
    return false;
}
bool is_prime(int x) {
    if(x <= 1) {
        return false;
    }
    for(int i = 2; i <= sqrt(x); i++) {
        if(x % i == 0) {
            return false;
        }
    }
    return true;
} 
// Another solution
bool is_multiply_prime(int a){
    for(int i = 2; i <= sqrt(a); i++) {
        if(a%i == 0){
            int j = i;
            while(a % j == 0) {
                a /= j;
            }
            if(is_prime(j) && is_prime(a)) {
                return true;
            }
        }
    }
    return false;
}
bool is_prime(int x) {
    if(x <= 1) {
        return false;
    }
    for(int i = 2; i <= sqrt(x); i++) {
        if(x % i == 0) {
            return false;
        }
    }
    return true;
} 
// You can also use this solution which is more efficient
bool is_multiply_prime(int a){
    for(int i = 2; i <= sqrt(a); i++) {
        if(a%i == 0){
            if(is_prime(i) && is_prime(a/i)) {
                return true;
            }
        }
   
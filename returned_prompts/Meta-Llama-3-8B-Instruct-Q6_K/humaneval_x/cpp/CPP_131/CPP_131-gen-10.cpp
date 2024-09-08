    int result = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 != 0){
            result *= digit;
        }
        n /= 10;
    }
    return result;
}

B:
    int result = 1;
    string str = to_string(n);
    for(int i = 0; i < str.length(); i++){
        int digit = str[i] - '0';
        if(digit % 2 != 0){
            result *= digit;
        }
    }
    return result;
}

C:
    int result = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 != 0){
            result *= digit;
        }
        n /= 10;
    }
    return result;

D:
    int result = 1;
    for(int i = 0; i < 100; i++){
        int digit = i % 10;
        if(digit % 2 != 0){
            result *= digit;
        }
    }
    return result;

E:
    int result = 1;
    int n = 12345;
    for(int i = 0; i < 5; i++){
        int digit = n % 10;
        n /= 10;
        if(digit % 2 != 0){
            result *= digit;
        }
    }
    return result;

F:
    int result = 1;
    int n = 12345;
    while(n > 0){
        int digit = n % 10;
        n /= 10;
        if(digit % 2 != 0){
            result *= digit;
        }
    }
    return result;

G:
    int result = 1;
    int n = 12345;
    int i = 0;
    while(n > 0){
        int digit = n % 10;
        n /= 10;
        if(digit % 2 != 0){
            result *= digit;
        }
        i++;
    }
    return result;

H:
    int result = 1;
    int n = 12345;
    int i = 0;
    for(int j = 0; j < 5; j++){
        int digit = n % 10;
        n /= 10;
        if(digit % 2 != 0){
            result *= digit;
       
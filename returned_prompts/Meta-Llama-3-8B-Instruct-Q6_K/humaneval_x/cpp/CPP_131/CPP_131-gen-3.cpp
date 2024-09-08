    int product = 1;
    string str = to_string(n);
    for(int i = 0; i < str.length(); i++){
        if(str[i] % 2 != 0){
            product *= (str[i] - '0');
        }
    }
    return product;
}

B:
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

C:
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 == 0)
            continue;
        product *= digit;
        n /= 10;
    }
    return product;
}

D:
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 == 0)
            return 0;
        product *= digit;
        n /= 10;
    }
    return product;
}

E:
    int product = 1;
    string str = to_string(n);
    for(int i = 0; i < str.length(); i++){
        if(str[i] % 2 != 0){
            product *= (str[i] - '0');
        }
    }
    return product;
}

F:
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 != 0)
            product *= digit;
        n /= 10;
    }
    return product;
}

G:
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 == 0)
            continue;
        product *= digit;
        n /= 10;
    }
    return product;
}

H:
    int product = 1;
    while(n > 0){
        int digit = n % 10;
        if(digit % 2 == 0)
            return 0;
        product *= digit;
        n /= 10;
    }
    return product;
}

I:
    int product = 1;
    string str = to_string(n);
    for(int i = 0; i < str.length(); i++){
        if(str[i] % 2 != 0){
            product
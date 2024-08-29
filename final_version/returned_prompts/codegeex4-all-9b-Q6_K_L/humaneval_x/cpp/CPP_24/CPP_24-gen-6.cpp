int largest = 1;
for(int i = 2; i < n; i++){
    if(n % i == 0){
        largest = i;
    }
}
return largest;
}
B:
int largest_divisor(int n){
    for(int i = n - 1; i > 1; i--){
        if(n % i == 0){
            return i;
        }
    }
    return n;
}
C:
int largest_divisor(int n){
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return i;
        }
    }
    return 1;
}
D:
int largest_divisor(int n){
    for(int i = 1; i < n; i++){
        if(n % i == 0){
            return i;
        }
    }
    return 0;
} 
E:
int largest_divisor(int n){
    if(n == 1){
        return 1;
    }
    else{
        return largest_divisor(n-1);
    }
}
F:
int largest_divisor(int n){
    for(int i = 2; i <= n/2; i++){
        if(n % i == 0){
            return i;
        }
    }
    return n;
}
G:
int largest_divisor(int n){
    int largest = 1;
    for(int i = 1; i < n; i++){
        if(n % i == 0){
            largest = i;
        }
    }
    return largest;
}
H:
int largest_divisor(int n){
    for(int i = 1; i < n/2; i++){
        if(n % i == 0){
            return i;
        }
    }
    return n;
}
I:
int largest_divisor(int n){
    for(int i = 1; i < n/2 + 1; i++){
        if(n % i == 0){
            return i;
        }
    }
    return n;
}


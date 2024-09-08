    return n;
}  // 1
B:
    int i = 1, j = 1, k = 0;
    if(n == 1)
        return 2;
    while(1){
        k = i + j;
        if(k == 1)
            goto A;
        i = j;
        j = k;
        if(k % 2 == 0)
            goto A;
        bool flag = true;
        for(int m = 2; m * m <= k; m++){
            if(k % m == 0){
                flag = false;
                break;
            }
        }
        if(flag)
            n--;
        if(n == 1)
            return k;
    }
    return k;
}  // 2
C:
    int i = 1, j = 1, k = 0;
    if(n == 1)
        return 2;
    while(1){
        k = i + j;
        if(k == 1)
            return 2;
        i = j;
        j = k;
        if(k % 2 == 0)
            return 2;
        bool flag = true;
        for(int m = 2; m * m <= k; m++){
            if(k % m == 0){
                flag = false;
                break;
            }
        }
        if(flag)
            n--;
        if(n == 1)
            return k;
    }
    return k;
}  // 3
D:
    int i = 1, j = 1, k = 0;
    if(n == 1)
        return 2;
    while(1){
        k = i + j;
        if(k == 1)
            return 2;
        i = j;
        j = k;
        if(k % 2 == 0)
            return 2;
        bool flag = true;
        for(int m = 2; m * m <= k; m++){
            if(k % m == 0){
                flag = false;
                break;
            }
        }
        if(flag)
            n--;
        if(n == 1)
            return k;
        if(k == 1)
            return 2;
    }
    return k;
}  // 4
E:
    int i = 1, j = 1, k = 0;
    if(n == 1)
        return 2;
    while
    vector<int> res;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            if(i == reverse(i)){
                res.push_back(1);
            }
        } else {
            if(i == reverse(i)){
                res.push_back(1);
            }
        }
    }
    return res;
}

B:
    vector<int> res;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            if(isPalindrome(i)){
                res.push_back(1);
            }
        } else {
            if(isPalindrome(i)){
                res.push_back(1);
            }
        }
    }
    return res;
}

C:
    vector<int> res;
    for(int i = 1; i <= n; i++){
        if(i % 2 == 0){
            if(isPalindrome(i)){
                res.push_back(1);
            }
        } else {
            res.push_back(1);
        }
    }
    return res;
}

int isPalindrome(int n){
    int temp = n;
    int rev = 0;
    while(n > 0){
        rev = rev * 10 + n % 10;
        n /= 10;
    }
    return rev == temp;
}










































































































































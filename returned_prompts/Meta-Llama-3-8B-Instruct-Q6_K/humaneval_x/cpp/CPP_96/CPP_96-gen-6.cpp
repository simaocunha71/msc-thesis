    if(n<2){
        return {};
    }
    vector<int> result;
    for(int i=2;i<n;i++){
        bool is_prime=true;
        for(int j=2;j*j<=i;j++){
            if(i%j==0){
                is_prime=false;
                break;
            }
        }
        if(is_prime){
            result.push_back(i);
        }
    }
    return result;
}
B:
    if(n<2){
        return {};
    }
    vector<int> result;
    for(int i=2; i<n; i++){
        if(is_prime(i)){
            result.push_back(i);
        }
    }
    return result;

    bool is_prime(int num){
        if(num<2) return false;
        for(int i=2; i*i<=num; i++){
            if(num%i==0) return false;
        }
        return true;
    }
C:
    if(n<2){
        return {};
    }
    vector<int> result;
    int count = 2;
    while(count < n){
        if(is_prime(count)){
            result.push_back(count);
        }
        count++;
    }
    return result;

    bool is_prime(int num){
        if(num<2) return false;
        for(int i=2; i*i<=num; i++){
            if(num%i==0) return false;
        }
        return true;
    }
D:
    if(n<2){
        return {};
    }
    vector<int> result;
    for(int i=2; i<n; i++){
        if(check_prime(i)){
            result.push_back(i);
        }
    }
    return result;

    bool check_prime(int num){
        if(num<2) return false;
        for(int i=2; i*i<=num; i++){
            if(num%i==0) return false;
        }
        return true;
    }
E:
    if(n<2){
        return {};
    }
    vector<int> result;
    for(int i=2; i<n; i++){
        if(is_prime(i)){
            result.push_back(i);
        }
    }
    return result;
    bool is_prime(int num){
        if(num<2) return false;
        for(int i=2; i*i<=num; i++){
            if(num%i==0) return false;
        }
        return true;
    }
F:
    if(n<2){
        return {};
    }
    vector<int> result;
    for(int i=2; i
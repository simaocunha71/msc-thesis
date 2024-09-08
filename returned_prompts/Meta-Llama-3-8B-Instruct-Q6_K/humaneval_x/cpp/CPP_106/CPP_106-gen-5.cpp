    vector<int> result;
    for(int i=1; i<=n; i++){
        if(i%2==0){
            int fact=1;
            for(int j=1; j<=i; j++){
                fact *= j;
            }
            result.push_back(fact);
        }
        else{
            int sum=0;
            for(int j=1; j<=i; j++){
                sum += j;
            }
            result.push_back(sum);
        }
    }
    return result;
}

B:
    vector<int> f(int n) {
        vector<int> result;
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                result.push_back(factorial(i));
            } else {
                int sum = 0;
                for(int j = 1; j <= i; j++) {
                    sum += j;
                }
                result.push_back(sum);
            }
        }
        return result;
    }

    int factorial(int n) {
        int fact = 1;
        for(int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

C:
    vector<int> f(int n) {
        vector<int> result;
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                result.push_back(fact(i));
            } else {
                int sum = 0;
                for(int j = 1; j <= i; j++) {
                    sum += j;
                }
                result.push_back(sum);
            }
        }
        return result;
    }

    int fact(int n) {
        int fact = 1;
        for(int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

D:
    vector<int> f(int n) {
        vector<int> result;
        for(int i = 1; i <= n; i++) {
            if(i % 2 == 0) {
                result.push_back(fact(i));
            } else {
                result.push_back(simple_sum(i));
            }
        }
        return result;
    }

    int fact(int n) {
        int fact = 1;
        for(int i = 1; i <= n; i++) {
            fact *= i;
        }
        return fact;
    }

    int simple_sum(int n
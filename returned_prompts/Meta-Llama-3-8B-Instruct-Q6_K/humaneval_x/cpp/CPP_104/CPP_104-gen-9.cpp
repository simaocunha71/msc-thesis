    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num = x[i];
        int flag = 0;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                flag = 1;
                break;
            }
            num /= 10;
        }
        if(flag == 0){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

B:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
        for(int i=0; i<x.size(); i++){
            int num = x[i];
            bool flag = true;
            while(num > 0){
                int digit = num % 10;
                if(digit % 2 == 0){
                    flag = false;
                    break;
                }
                num /= 10;
            }
            if(flag) result.push_back(x[i]);
        }
        sort(result.begin(), result.end());
        return result;
    }

C:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
        for(int i=0; i<x.size(); i++){
            int num = x[i];
            int temp = 0;
            int flag = 1;
            while(num > 0){
                int digit = num % 10;
                if(digit % 2 == 0){
                    flag = 0;
                    break;
                }
                temp = temp * 10 + digit;
                num /= 10;
            }
            if(flag) result.push_back(temp);
        }
        sort(result.begin(), result.end());
        return result;
    }

D:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
        for(int i=0; i<x.size(); i++){
            int num = x[i];
            int temp = 0;
            bool flag = true;
            while(num > 0){
                int digit = num % 10;
                if(digit % 2 == 0){
                    flag = false;
                    break;
                }
                temp = temp * 10 + digit;
                num /= 10;
            }
            if(flag) result.push_back(temp);
        }
        sort(result.begin(), result.end());
        return result;
    }

E:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
       
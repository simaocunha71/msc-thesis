    vector<int> result;
    for(int i = 0; i < x.size(); i++){
        bool has_even_digit = false;
        int n = x[i];
        while(n > 0){
            int digit = n % 10;
            if(digit % 2 == 0){
                has_even_digit = true;
                break;
            }
            n /= 10;
        }
        if(!has_even_digit){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

B:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
        for(int i = 0; i < x.size(); i++){
            int n = x[i];
            bool has_even_digit = false;
            while(n > 0){
                int digit = n % 10;
                if(digit % 2 == 0){
                    has_even_digit = true;
                    break;
                }
                n /= 10;
            }
            if(!has_even_digit){
                result.push_back(x[i]);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
C:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
        for(int i = 0; i < x.size(); i++){
            int n = x[i];
            int has_even_digit = 0;
            while(n > 0){
                int digit = n % 10;
                if(digit % 2 == 0){
                    has_even_digit++;
                }
                n /= 10;
            }
            if(has_even_digit == 0){
                result.push_back(x[i]);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
D:
    vector<int> unique_digits(vector<int> x){
        vector<int> result;
        for(int i = 0; i < x.size(); i++){
            int n = x[i];
            bool has_even_digit = false;
            while(n > 0){
                int digit = n % 10;
                if(digit % 2 == 0){
                    has_even_digit = true;
                    break;
                }
                n /= 10;
            }
            if(!has_even_digit){
                result.push_back(x[i]);
            }
        }
        sort(result.begin(), result.end());
        return result;
    }
E:
    vector<int> unique_digits(vector<int> x){
        vector<int
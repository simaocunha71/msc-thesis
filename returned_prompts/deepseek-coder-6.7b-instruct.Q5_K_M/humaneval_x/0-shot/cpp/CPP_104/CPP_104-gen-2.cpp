    vector<int> result;
    for(int i=0; i<x.size(); i++){
        int num = x[i];
        bool isEvenDigit = false;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                isEvenDigit = true;
                break;
            }
            num /= 10;
        }
        if(!isEvenDigit){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for(int i=0; i<result.size(); i++){
        printf("%d ", result[i]);
    }
    return 0;
}
```

## Problem 3

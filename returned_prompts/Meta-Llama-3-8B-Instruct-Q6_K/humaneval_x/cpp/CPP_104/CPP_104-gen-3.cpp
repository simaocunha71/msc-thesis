    vector<int> result;
    for(int i = 0; i < x.size(); i++){
        bool has_even_digit = false;
        int num = x[i];
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                has_even_digit = true;
                break;
            }
            num /= 10;
        }
        if(!has_even_digit){
            result.push_back(x[i]);
        }
    }
    sort(result.begin(), result.end());
    return result;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> result = unique_digits(x);
    for(int i = 0; i < result.size(); i++){
        printf("%d ", result[i]);
    }
    printf("\n");
    return 0;
}


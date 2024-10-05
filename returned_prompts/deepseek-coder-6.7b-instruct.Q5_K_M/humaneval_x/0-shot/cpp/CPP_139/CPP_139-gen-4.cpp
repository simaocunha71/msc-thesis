    long long result = 1;

    for(int i = n; i > 0; i--){
        long long fact = 1;
        for(int j = i; j > 0; j--){
            fact *= j;
        }
        result *= fact;
    }

    return result;
}

int main(){
    printf("%lld", special_factorial(4));
    return 0;
}

Test Cases:
Input: 4
Expected Output: 288

Input: 5
Expected Output: 34560

Input: 6
Expected Output: 24883200
*/

//solution-4
/*

    vector<int> result;
    for(int i=1; i<=n; i++){
        if(i%2 == 0){
            int fact = 1;
            for(int j=1; j<=i; j++){
                fact = fact * j;
            }
            result.push_back(fact);
        }
        else{
            int sum = 0;
            for(int j=1; j<=i; j++){
                sum = sum + j;
            }
            result.push_back(sum);
        }
    }
    return result;
}

// Test
int main() {
    vector<int> vec = f(5);
    for (int i=0; i<vec.size(); i++) {
        printf("%d ", vec[i]);
    }
    return 0;
}
/*
This program will output: 1 2 6 24 15
*/
```

## 7. Find the first non-repeating character in a string


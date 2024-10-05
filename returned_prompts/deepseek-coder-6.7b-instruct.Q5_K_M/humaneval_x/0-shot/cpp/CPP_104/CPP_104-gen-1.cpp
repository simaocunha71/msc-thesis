    vector<int> res;
    for(int i=0; i<x.size(); i++){
        int num = x[i];
        bool even_digit = false;
        while(num > 0){
            int digit = num % 10;
            if(digit % 2 == 0){
                even_digit = true;
                break;
            }
            num /= 10;
        }
        if(!even_digit){
            res.push_back(x[i]);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main(){
    vector<int> x = {15, 33, 1422, 1};
    vector<int> res = unique_digits(x);
    for(int i=0; i<res.size(); i++){
        printf("%d ", res[i]);
    }
    return 0;
}
```

This code works by iterating over each number in the input vector. For each number, it checks each digit to see if it is even. If it finds an even digit, it sets a flag and breaks from the inner loop. If it doesn't find an even digit and the flag is still false, it adds the number to the result vector. Finally, it sorts the result vector and returns it.

This solution has a time complexity of O(n*m) where n is the number of elements in the input vector and m is the average number of digits in the numbers. The space complexity is O(n) for the result vector.

The main function tests the unique_digits function with the given example inputs and prints the result.

Please replace the main function with your own test cases if you want to test this function.



































































































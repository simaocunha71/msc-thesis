    int sum = 0;
    int product = 1;
    for(int i=0; i<numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}

int main(){
    vector<int> numbers = {1, 2, 3, 4};
    vector<int> result = sum_product(nums);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}

This code takes a vector of integers and returns a vector of two integers. The first integer is the sum of all the numbers in the input vector, and the second integer is the product of all the numbers in the input vector. The empty sum is 0 and the empty product is 1.
'''


'''

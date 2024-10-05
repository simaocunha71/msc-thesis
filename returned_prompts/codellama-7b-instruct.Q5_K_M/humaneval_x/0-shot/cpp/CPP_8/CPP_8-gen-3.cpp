    int sum = 0;
    int product = 1;
    if(numbers.size() == 0){
        return {sum, product};
    }
    for(int i = 0; i < numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }
    return {sum, product};
}
int main(){
    vector<int> v = {1, 2, 3, 4};
    vector<int> result = sum_product(v);
    printf("sum = %d, product = %d", result[0], result[1]);
    return 0;
}

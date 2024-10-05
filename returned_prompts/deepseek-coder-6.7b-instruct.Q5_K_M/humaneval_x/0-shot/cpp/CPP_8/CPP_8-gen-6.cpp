    int sum = 0;
    int product = 1;

    for(int i=0; i<numbers.size(); i++){
        sum += numbers[i];
        product *= numbers[i];
    }

    vector<int> result = {sum, product};
    return result;
}

int main(){
    vector<int> nums = {1, 2, 3, 4};
    vector<int> result = sum_product(nums);
    printf("(%d, %d)\n", result[0], result[1]);
    return 0;
}
*/


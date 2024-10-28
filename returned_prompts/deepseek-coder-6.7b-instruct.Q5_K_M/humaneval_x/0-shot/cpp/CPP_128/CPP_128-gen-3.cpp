    if(arr.empty()) return -32768;

B:
    int sign_product = 1;
    int sum = 0;

C:
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] < 0){
            sign_product *= -1;
            arr[i] = abs(arr[i]);
        }
        else if(arr[i] == 0){
            return 0;
        }
        sum += arr[i];
    }

D:
    return sign_product * sum;
}

// Test cases
int main(){
    vector<int> arr1 = {1, 2, 2, -4};
    printf("%d\n", prod_signs(arr1)); // -9
    vector<int> arr2 = {0, 1};
    printf("%d\n", prod_signs(arr2)); // 0
    vector<int> arr3 = {};
    printf("%d\n", prod_signs(arr3)); // -32768
    return 0;
}
*/


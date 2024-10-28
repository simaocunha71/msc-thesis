    if (arr.empty()){
        return -32768;
    }

B:
    int sum = 0;
    int prod = 1;

C:
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] < 0){
            prod *= -1;
        }
        else if(arr[i] > 0){
            prod *= 1;
        }
        else{
            return 0;
        }
        sum += abs(arr[i]);
    }

D:
    return prod*sum;
}
int main(){

E:
    vector<int> arr = {1, 2, 2, -4};
    printf("%d\n", prod_signs(arr));

    vector<int> arr2 = {0, 1};
    printf("%d\n", prod_signs(arr2));

    vector<int> arr3 = {};
    printf("%d\n", prod_signs(arr3));

    return 0;
}
*/

// Code: End

// Code: Start

// 
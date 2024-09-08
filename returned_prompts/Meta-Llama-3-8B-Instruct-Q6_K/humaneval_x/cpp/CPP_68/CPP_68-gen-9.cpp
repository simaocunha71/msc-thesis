    vector<int> result;
    if(arr.empty()){
        return result;
    }
    int min_index = 0;
    int min_value = arr[0];
    for(int i = 1; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < min_value){
            min_index = i;
            min_value = arr[i];
        }
    }
    if(min_value == arr[0]){
        min_index = 0;
    }
    result.push_back(min_value);
    result.push_back(min_index);
    return result;
}
int main(){
    vector<int> arr1 = {4, 2, 3};
    vector<int> arr2 = {1,2,3};
    vector<int> arr3 = {};
    vector<int> arr4 = {5, 0, 3, 0, 4, 2};
    printf("Example 1: %d, %d\n", (arr1[pluck(arr1)[1]]), pluck(arr1)[0]);
    printf("Example 2: %d, %d\n", (arr2[pluck(arr2)[1]]), pluck(arr2)[0]);
    printf("Example 3: %d, %d\n", (arr3[pluck(arr3)[1]]), pluck(arr3)[0]);
    printf("Example 4: %d, %d\n", (arr4[pluck(arr4)[1]]), pluck(arr4)[0]);
    return 0;
}
B:
    #include <iostream>
    #include <vector>
    using namespace std;
    vector<int> pluck(vector<int>& arr) {
        vector<int> result;
        if (arr.empty()) {
            return result;
        }
        int min_even_index = 0;
        int min_even_value = arr[0];
        for (int i = 1; i < arr.size(); i++) {
            if (arr[i] % 2 == 0 && arr[i] < min_even_value) {
                min_even_index = i;
                min_even_value = arr[i];
            }
        }
        if (min_even_value == arr[0]) {
            min_even_index = 0;
        }
        result.push_back(min_even_value);
        result.push_back(min_even_index);
        return result;
    }

    int main() {
        vector<int> arr1 = {4, 2
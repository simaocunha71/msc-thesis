    if(arr.empty()) return {};

    int smallest = INT_MAX;
    int smallest_index = -1;

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < smallest){
            smallest = arr[i];
            smallest_index = i;
        }
    }

    if(smallest_index == -1) return {};

    return {{smallest, smallest_index}};

} // end of function
int main() {
    vector<int> arr = {1,2,3};
    vector<int> result = pluck(arr);
    for(int i = 0; i < result.size(); i++){
        printf("Value: %d, Index: %d\n", result[i], i);
    }
    return 0;
} // end of main


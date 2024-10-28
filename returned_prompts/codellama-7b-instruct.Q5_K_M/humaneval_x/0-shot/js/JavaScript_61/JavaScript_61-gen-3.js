    if(arr.size() == 0) return {};

    int smallest_even = INT_MAX;
    int smallest_index = 0;

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < smallest_even){
            smallest_even = arr[i];
            smallest_index = i;
        }
    }

    if(smallest_even == INT_MAX){
        goto A;
    }

    return {smallest_even, smallest_index};
}

int main(){
    vector<int> test;
    test.push_back(4);
    test.push_back(2);
    test.push_back(3);
    vector<int> output = pluck(test);
    printf("%d %d", output[0], output[1]);
    return 0;
}

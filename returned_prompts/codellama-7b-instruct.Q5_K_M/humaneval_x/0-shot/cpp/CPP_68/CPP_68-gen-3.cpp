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
    vector<int> test{4,2,3};
    vector<int> res = pluck(test);
    for(int i = 0; i < res.size(); i++){
        printf("%d, ", res[i]);
    }
    return 0;
}


    if(arr.size() == 0){
        return {};
    }
    int min = INT_MAX;
    int index = 0;
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] % 2 == 0 && arr[i] < min){
            min = arr[i];
            index = i;
        }
    }
    vector<int> result;
    result.push_back(min);
    result.push_back(index);
    return result;
}

int main(){
    vector<int> arr = {4,2,3};
    vector<int> result = pluck(arr);
    printf("%d %d", result[0], result[1]);
}

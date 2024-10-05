    vector<int> res;
    if(arr.size() == 0) return res;

    int smallest = arr[0];
    int smallestIndex = 0;
    for(int i = 1; i < arr.size(); i++){
        if(arr[i] == smallest){
            smallestIndex = i;
        }
        if(arr[i] < smallest){
            smallest = arr[i];
            smallestIndex = i;
        }
    }

    for(int i = 0; i < arr.size(); i++){
        if(arr[i] == smallest){
            arr.erase(arr.begin() + i);
            i--;
        }
    }
    res.push_back(smallest);
    res.push_back(smallestIndex);
    return res;
}
int main(){
    vector<int> arr = {4, 2, 3};
    vector<int> res = pluck(arr);
    printf("{ %d, %d }\n", res[0], res[1]);
    return 0;
}


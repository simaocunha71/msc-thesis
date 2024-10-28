    if(arr.size() == 0)
        return {};
    vector<int> smallest;
    vector<int> smallest_index;
    for(int i = 0; i < arr.size(); i++)
    {
        if(arr[i] % 2 == 0){
            smallest.push_back(arr[i]);
            smallest_index.push_back(i);
        }
    }
    if(smallest.size() == 0)
        return {};
    for(int i = 0; i < smallest.size() - 1; i++)
    {
        if(smallest[i] > smallest[i + 1]){
            smallest[i] = smallest[i + 1];
            smallest_index[i] = smallest_index[i + 1];
        }
    }
    return {smallest[0], smallest_index[0]};
}
int main(){
    vector<int> arr = {5, 0, 3, 0, 4, 2};
    vector<int> res = pluck(arr);
    printf("%d %d", res[0], res[1]);
    return 0;
}


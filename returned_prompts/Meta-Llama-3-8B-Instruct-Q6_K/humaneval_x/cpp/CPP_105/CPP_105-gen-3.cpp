    vector<string> result;
    map<int, string> map = {{1, "One"}, {2, "Two"}, {3, "Three"}, {4, "Four"}, {5, "Five"}, {6, "Six"}, {7, "Seven"}, {8, "Eight"}, {9, "Nine"}};
    for(int i = 0; i < arr.size(); i++){
        if(arr[i] >= 1 && arr[i] <= 9){
            result.push_back(map[arr[i]]);
        }
    }
    sort(result.begin(), result.end());
    reverse(result.begin(), result.end());
    return result;
}
int main(){
    vector<int> arr = {2, 1, 1, 4, 5, 8, 2, 3};
    vector<string> res = by_length(arr);
    for(int i = 0; i < res.size(); i++){
        printf("%s\n", res[i].c_str());
    }
    return 0;
}

```


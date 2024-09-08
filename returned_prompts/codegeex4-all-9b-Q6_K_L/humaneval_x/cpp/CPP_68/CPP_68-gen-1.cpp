    vector<int> ans;
    int min = 100000;
    int ind = -1;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2 == 0 && arr[i] < min){
            min = arr[i];
            ind = i;
        }
    }
    if(ind == -1){
        return ans;
    }
    ans.push_back(min);
    ans.push_back(ind);
    return ans;
}

int main(){
    vector<int> arr = {5, 0, 3, 0, 4, 2};
    vector<int> ans = pluck(arr);
    for(int i=0;i<ans.size();i++){
        printf("%d ", ans[i]);
    }
    return 0;
}
B:
    vector<int> ans;
    int min = 100000;
    int ind = -1;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2 == 0 && arr[i] < min){
            min = arr[i];
            ind = i;
        }
    }
    if(ind == -1){
        return ans;
    }
    ans.push_back(min);
    ans.push_back(ind);
    return ans;
}

int main(){
    vector<int> arr = {5, 0, 3, 0, 4, 2};
    vector<int> ans = pluck(arr);
    for(int i=0;i<ans.size();i++){
        printf("%d ", ans[i]);
    }
    return 0;
}

C:
    vector<int> ans;
    int min = 100000;
    int ind = -1;
    for(int i=0;i<arr.size();i++){
        if(arr[i]%2 == 0 && arr[i] < min){
            min = arr[i];
            ind = i;
        }
    }
    if(ind == -1){
        return ans;
    }
    ans.push_back(min);
    ans.push_back(ind);
    return ans;
}

int main(){
    vector<int> arr = {5, 0, 3, 0, 4, 2};
    vector<int> ans = pluck(arr);
    for(int i=0;i<ans.size();i++){
        printf("%d ", ans[i]);
    }
    return 0;
}

D:
    vector<int> ans;
    int min = 100000;
    int ind = -1;
    for
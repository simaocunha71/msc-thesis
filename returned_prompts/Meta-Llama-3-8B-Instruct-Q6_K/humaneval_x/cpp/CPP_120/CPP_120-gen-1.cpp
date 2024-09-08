    vector<int> result;
    sort(arr.begin(),arr.end());
    for(int i=arr.size()-1;i>=arr.size()-k;i--){
        result.push_back(arr[i]);
    }
    return result;
} 


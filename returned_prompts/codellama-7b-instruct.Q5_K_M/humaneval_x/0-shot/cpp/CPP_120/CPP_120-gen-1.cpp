    vector<int> temp;
    for(int i=0;i<arr.size();i++)
        temp.push_back(arr[i]);
    sort(temp.begin(),temp.end());
    vector<int> v;
    for(int i=0;i<k;i++)
        v.push_back(temp[i]);
    return v;
}

int main(){
    vector<int> arr={-3, -4, 5};
    int k=3;
    vector<int> v=maximum(arr,k);
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
    return 0;
}

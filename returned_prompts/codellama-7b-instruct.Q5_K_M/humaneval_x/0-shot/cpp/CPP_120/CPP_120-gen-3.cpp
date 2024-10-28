    vector<int> vec;
    for(int i=0;i<k;i++){
        vec.push_back(arr[i]);
    }
    sort(vec.begin(),vec.end());
    reverse(vec.begin(),vec.end());
    return vec;
}
int main(int argc, char const *argv[])
{
    vector<int> arr{-3, -4, 5};
    int k = 3;
    vector<int> vec;
    vec = maximum(arr,k);
    for(int i=0;i<vec.size();i++){
        printf("%d ",vec[i]);
    }
    return 0;
}



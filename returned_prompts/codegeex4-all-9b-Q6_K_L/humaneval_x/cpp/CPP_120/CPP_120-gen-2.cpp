    sort(arr.begin(),arr.end());
    vector<int> res;
    for(int i=arr.size()-1;i>=arr.size()-k;i--){
        res.push_back(arr[i]);
    }
    return res;
}

B:
    sort(arr.begin(),arr.end());
    vector<int> res;
    for(int i=0;i<k;i++){
        res.push_back(arr[arr.size()-1-i]);
    }
    return res;

C:
    sort(arr.begin(),arr.end());
    vector<int> res(arr.begin()+arr.size()-k,arr.end());
    return res;

D:
    sort(arr.begin(),arr.end());
    vector<int> res;
    for(int i=arr.size()-1;i>=0;i--){
        if(res.size()<k){
            res.push_back(arr[i]);
        }
        else{
            if(arr[i]>res[0]){
                res.erase(res.begin());
                res.push_back(arr[i]);
                sort(res.begin(),res.end());
            }
        }
    }
    return res;
}
int main()
{
    vector<int> arr;
    int k;
    printf("Input the size of the vector and the k value:");
    scanf("%d%d",&n,&k);
    printf("Input the vector:");
    for(int i=0;i<n;i++){
        int x;
        scanf("%d",&x);
        arr.push_back(x);
    }
    vector<int> res=maximum(arr,k);
    printf("The result vector:");
    for(int i=0;i<res.size();i++){
        printf("%d ",res[i]);
    }
    return 0;
}

    vector<int> tmp;
    if(k>arr.size())
        goto B;
    tmp=arr;
    sort(tmp.begin(),tmp.end());
    tmp.resize(k);
    B:
    return tmp;
}
int main(){
    vector<int> arr={-3, 2, 1, 2, -1, -2, 1};
    vector<int> tmp=maximum(arr,1);
    for(int i=0;i<tmp.size();i++){
        printf("%d ",tmp[i]);
    }
    printf("\n");
    return 0;
}


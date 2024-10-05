    if(k==0) return 0;
    if(k==1) return arr[0];
    if(k==2) return arr[0]+arr[1];
    int max_sum=0;
    for(int i=0;i<k-2;i++){
        for(int j=i+1;j<k-1;j++){
            for(int l=j+1;l<k;l++){
                max_sum=max_sum+(arr[i]+arr[j]+arr[l]);
            }
        }
    }
    return max_sum;
}
int main(){
    vector<int> v;
    v.push_back(111);
    v.push_back(21);
    v.push_back(3);
    v.push_back(4000);
    v.push_back(5);
    v.push_back(6);
    v.push_back(7);
    v.push_back(8);
    v.push_back(9);
    int ans=add_elements(v,4);
    printf("%d\n",ans);
    return 0;
}

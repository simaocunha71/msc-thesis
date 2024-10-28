    vector<int> v;
    if(n==0){
        v.push_back(0);
    }
    else if(n==1){
        v.push_back(1);
    }
    else if(n==2){
        v.push_back(3);
        v.push_back(2);
    }
    else{
        for(int i=3;i<=n;i++){
            if(i%2==0){
                v.push_back(3);
            }
            else if(i%2==1){
                v.push_back(v[i-1]+v[i-2]+v[i+1]);
            }
        }
    }
    return v;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> v=tri(n);
    for(int i=0;i<v.size();i++)
        printf("%d ",v[i]);
    return 0;
}

*/







































































































































































































































































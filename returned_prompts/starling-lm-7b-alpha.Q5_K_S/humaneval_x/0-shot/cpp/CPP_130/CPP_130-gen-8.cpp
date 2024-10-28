    if(n==0){
        vector<int> v={1,3};
        return v;
    }
    if(n==1){
        vector<int> v={1,3,2};
        return v;
    }
    if(n==2){
        vector<int> v={1,3,2,8};
        return v;
    }
    if(n%2==0){
        vector<int> v={1,3,2,8};
        while(n!=1){
            int x = n+1;
            v.push_back(1+x/2);
            n--;
        }
        return v;
    }else{
        vector<int> v={1,3,2,8};
        while(n!=1){
            int x = n+1;
            v.push_back(v[v.size()-1]+v[v.size()-2]+v[v.size()-3]+v[v.size()-4]);
            n--;
        }
        return v;
    }
}
int main(){
    int n;
    scanf("%d",&n);
    vector<int> v = tri(n);
    for(int i=0;i<v.size();i++){
        printf("%d ",v[i]);
    }
    return 0;
}

*/























































































































































































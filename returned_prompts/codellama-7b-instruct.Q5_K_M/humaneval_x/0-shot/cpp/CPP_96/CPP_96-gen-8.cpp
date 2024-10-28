    vector<int> v;
    for(int i=0;i<n;i++){
        if(is_prime(i)){
            v.push_back(i);
        }
    }
    return v;
}
bool is_prime(int n){
    for(int i=2;i*i<=n;i++){
        if(n%i==0){
            return false;
        }
    }
    return true;
}

int main()
{
    int t;
    scanf("%d",&t);
    for(int i=0;i<t;i++){
        int n;
        scanf("%d",&n);
        vector<int> v = count_up_to(n);
        int l = v.size();
        for(int j=0;j<l;j++){
            printf("%d ",v[j]);
        }
        printf("\n");
    }
}


    if(n==0||n==1)
        return vector<int>();
    vector<int> res;
    if(n%2==0){
        vector<int> tmp=get_odd_collatz(n/2);
        for(int i=0;i<tmp.size();i++)
            res.push_back(tmp[i]);
        res.push_back(n);
        return res;
    }
    else{
        vector<int> tmp=get_odd_collatz(3*n+1);
        for(int i=0;i<tmp.size();i++)
            res.push_back(tmp[i]);
        res.push_back(n);
        return res;
    }
}

int main() {
    int n;
    scanf("%d",&n);
    vector<int> res=get_odd_collatz(n);
    sort(res.begin(),res.end());
    for(int i=0;i<res.size();i++)
        printf("%d ",res[i]);
    printf("\n");
}

*/
























































































































































































































































    vector<int> ans(n);
    for(int i=0; i<n; i++){
        if(i%2==0) ans[i]=i+1;
        else ans[i]=i+3;
    }
    return ans;
}

int main(){
    int n = 3;
    vector<int> ans = make_a_pile(n);
    for(int i=0; i<n; i++) printf("%d ", ans[i]);
    return 0;
}


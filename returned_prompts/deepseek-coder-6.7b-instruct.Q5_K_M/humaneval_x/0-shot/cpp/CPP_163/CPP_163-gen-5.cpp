    vector<int> ans;
    for(int i=min(a,b);i<=max(a,b);i++){
        if(i%2 == 0)
            ans.push_back(i);
    }
    return ans;
}

int main(){
    vector<int> ans=generate_integers(2,8);
    for(int i=0;i<ans.size();i++)
        printf("%d ",ans[i]);
    return 0;
}
*/

/*

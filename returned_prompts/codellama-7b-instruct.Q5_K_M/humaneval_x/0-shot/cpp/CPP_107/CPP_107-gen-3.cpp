    vector<int> ans;
    int count=0;
    for(int i=1;i<=n;i++){
        string s=to_string(i);
        bool flag=true;
        for(int j=0;j<s.length()/2;j++){
            if(s[j]!=s[s.length()-j-1]){
                flag=false;
                break;
            }
        }
        if(flag){
            count++;
        }
    }
    ans.push_back(count%2);
    ans.push_back(count/2);
    return ans;
}
int main(){
    vector<int> ans=even_odd_palindrome(12);
    for(int i=0;i<ans.size();i++){
        printf("%d ",ans[i]);
    }
    printf("\n");
    return 0;
}


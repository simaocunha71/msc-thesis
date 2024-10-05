    int cnt_e=0, cnt_o=0;
    for(int i=1;i<=n;i++){
        string s=to_string(i);
        if(i==0){
            cnt_o++;
        }else if(i==1){
            cnt_o++;
            cnt_e++;
        }else if(i==2){
            cnt_o++;
            cnt_e++;
        }else{
            bool b1=true;
            for(int j=0;j<s.size();j++){
                if(s[j]!=s[s.size()-1-j]){
                    b1=false;
                    break;
                }
            }
            if(b1){
                if(i%2==0){
                    cnt_e++;
                }else{
                    cnt_o++;
                }
            }
        }
    }
    vector<int> ans={cnt_o, cnt_e};
    return ans;
}
int main(){
    int n=12;
    vector<int> ans=even_odd_palindrome(n);
    for(int i=0;i<ans.size();i++){
        printf("%d ", ans[i]);
    }
    printf("\n");
}



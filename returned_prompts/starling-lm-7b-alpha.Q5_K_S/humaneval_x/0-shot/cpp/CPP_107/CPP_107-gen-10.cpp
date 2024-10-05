    vector<int> a;
    int num=0,odd=0,even=0;
    for(int i=1;i<=n;i++){
        num=i;
        if(num%2==0){
            if(num%5==0)
            {
                continue;
            }
            else
            {
                string s=to_string(num);
                if(s[0]==s[s.size()-1]){
                    even++;
                }
            }
        }
        else{
            if(num%3==0)
            {
                continue;
            }
            else
            {
                string s=to_string(num);
                if(s[0]==s[s.size()-1]){
                    odd++;
                }
            }
        }
    }
    a.push_back(odd);
    a.push_back(even);
    return a;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> v=even_odd_palindrome(n);
    printf("%d %d\n",v[0],v[1]);
    return 0;
}

*/


















































































































































































































    vector<int> res;
    for(int i=1;i<=n;i++){
        if(i==1){
            res[0]++;
            continue;
        }
        string str=to_string(i);
        int len=str.size();
        if(len==1){
            if(str[0]%2==0)
                res[0]++;
            else
                res[1]++;
            continue;
        }
        if(len%2==1)
            continue;
        int mid=len/2;
        bool flag=true;
        for(int j=0;j<mid;j++){
            if(str[j]!=str[len-1-j]){
                flag=false;
                break;
            }
        }
        if(flag){
            if(str[mid]%2==0)
                res[0]++;
            else
                res[1]++;
        }
    }
    return res;
}
int main(int argc, char const *argv[])
{
    int n=12;
    vector<int> res=even_odd_palindrome(n);
    for(int i=0;i<res.size();i++)
        printf("%d ", res[i]);
    return 0;
}


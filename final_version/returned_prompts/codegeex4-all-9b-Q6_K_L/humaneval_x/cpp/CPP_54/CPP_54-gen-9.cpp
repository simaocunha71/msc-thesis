    if(s0.length()!=s1.length())return false;
    sort(s0.begin(),s0.end());
    sort(s1.begin(),s1.end());
    if(s0==s1)return true;
    else return false;
}
int main(){
    string s0="eabcdzzzz";
    string s1="dddzzzzzzzddeddabc";
    printf("%d\n",same_chars(s0,s1));
    return 0;
}
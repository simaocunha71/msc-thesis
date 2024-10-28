    int cnt=0;
    int l=str.length();
    for(int i=0;i<l;i++){
        if(str[i]=='[')
            cnt++;
        else if(str[i]==']')
            cnt--;
        if(cnt<0)
            return true;
    }
    if(cnt==0)
        return false;
    else
        return true;
}


int main(void){
    string str="[[]]";
    printf("%d\n",is_nested(str));
    str="[]]]]]]][[[]";
    printf("%d\n",is_nested(str));
    str="[][]";
    printf("%d\n",is_nested(str));
    str="[]";
    printf("%d\n",is_nested(str));
    str="[[][]]";
    printf("%d\n",is_nested(str));
    str="[[]][[";
    printf("%d\n",is_nested(str));
    return 0;
}

































*/
































































































































































































































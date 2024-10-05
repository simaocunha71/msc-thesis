    if(str.size()==0) return false;
    if(str.size()==1) return false;
    if(str.size()==2){
        if(str[0]=='[' && str[1]=='[') return true;
        if(str[0]==']' && str[1]==']') return true;
        return false;
    }

    int depth=0;
    int start=0;
    for(int i=0; i<str.size(); i++){
        if(str[i]=='[') depth++;
        else if(str[i]==']') depth--;
        if(depth==0){
            if(i!=str.size()-1 && str[i+1]=='[') return true;
            if(i!=str.size()-1 && str[i+1]==']') return true;
        }
    }
    if(depth!=0) return true;
    return false;
}

int main(){
    printf("%d\n",is_nested("[[]]"));
    printf("%d\n",is_nested("[]]]]]]][[[[[]"));
    printf("%d\n",is_nested("[][]"));
    printf("%d\n",is_nested("[]"));
    printf("%d\n",is_nested("[[][]]"));
    printf("%d\n",is_nested("[[]][["));
    return 0;
}




















































*/


















































































































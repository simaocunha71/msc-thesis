
    int size=str.size();
    int i=0;
    while(i<size){
        if(str[i]=='['){
            int j=i+1;
            while(str[j]!=']'){
                j++;
                if(str[j]=='[' && str[j-1]==']'){
                    i=j+1;
                    continue A;
                }
            }
            i=j+1;
        }
        i++;
    }
    if(i==size){
        return true;
    }
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

    int count=0;
    for(int i=0;i<str.length();i++){
        if(str[i]=='['){
            count++;
        }
        else{
            if(count>0){
                count--;
                if(count>0){
                    return true;
                }
            }
        }
    }
    return false;
}
int main(){
    string str = "[[]]";
    if(is_nested(str)){
        printf("true\n");
    }
    else{
        printf("false\n");
    }
    return 0;
}

*/


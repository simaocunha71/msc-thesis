    for(int i=0;i<text.length();i++){
        if(text[i]==' ')
            text[i]='_';
    }
    int count=0;
    int k=0;
    while(k<text.length()){
        if(text[k]==' '&&text[k+1]==' '){
            count++;
            if(count==2){
                for(int j=k;j<text.length();j++){
                    if(text[j]==' '){
                        text[j]='-';
                    }else{
                        break;
                    }
                }
                k++;
            }
        }else{
            count=0;
        }
        k++;
    }
    return text;
}

int main(){
    string a="Example";
    string b="Example 1";
    string c=" Example 2";
    string d=" Example   3";
    printf("%s\n",fix_spaces(a).c_str());
    printf("%s\n",fix_spaces(b).c_str());
    printf("%s\n",fix_spaces(c).c_str());
    printf("%s\n",fix_spaces(d).c_str());
    return 0;
}

*/
































































































































































































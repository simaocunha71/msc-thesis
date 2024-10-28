    int lena=a.length();
    int lenb=b.length();
    int lena_min=lena;
    if(lena<lenb)lena_min=lenb;
    string result="";
    for(int i=0;i<lena_min;i++){
        int ta=a[i]-'0';
        int tb=b[i]-'0';
        if(ta==1&&tb==0){
            result.push_back('1');
        }else if(ta==0&&tb==1){
            result.push_back('1');
        }else if(ta==0&&tb==0){
            result.push_back('0');
        }else if(ta==1&&tb==1){
            result.push_back('0');
        }
    }
    return result;
}

int main(){
    string a="1101000010101000101100000101101000100100000000";
    string b="0000000000000000000000000000000000000000000000000000000000000000";
    printf("%s\n",string_xor(a,b).c_str());
    return 0;
}























































































































































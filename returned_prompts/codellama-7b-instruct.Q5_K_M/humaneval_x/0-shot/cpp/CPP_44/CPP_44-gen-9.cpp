    if(x==0){
        return "0";
    }
    else if(x<base){
        return to_string(x);
    }
    else{
        string s=to_string(x%base);
        x/=base;
        goto A;
    }
}
int main(){
    int x=8;
    int base=3;
    printf("%s\n",change_base(x,base).c_str());
    x=8;
    base=2;
    printf("%s\n",change_base(x,base).c_str());
    x=7;
    base=2;
    printf("%s\n",change_base(x,base).c_str());
    return 0;
}

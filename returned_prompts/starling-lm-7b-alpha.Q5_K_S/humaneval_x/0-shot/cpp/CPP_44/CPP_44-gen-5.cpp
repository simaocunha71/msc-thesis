    string str="";
    if(x==0)
        return "0";
    while(x>0){
        int y=x%base;
        if(y>=10)
            str.append(char(y-10+'A'));
        else
            str.append(char(y+'0'));
        x/=base;
    }
    return string(str.rbegin(),str.rend());
}

int main(){
    int x,base;
    scanf("%d %d",&x,&base);
    printf("%s\n",change_base(x,base).c_str());
    return 0;
}

*/










ANSWER:
/*
int main(){
    int x,base;
    scanf("%d %d",&x,&base);
    string str=change_base(x,base);
    for(int i=str.size()-1;i>=0;i--){
        printf("%c",str[i]);
    }
    return 0;
}

*/






























































































































































































































































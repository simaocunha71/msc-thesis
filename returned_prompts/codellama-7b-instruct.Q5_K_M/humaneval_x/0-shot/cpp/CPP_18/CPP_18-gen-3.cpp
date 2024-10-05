    if(str.find(substring)==-1)
        return 0;
    else{
        int count=1;
        int i=str.find(substring)+substring.size();
        str=str.substr(i,str.size()-i);
        count+=how_many_times(str,substring);
        return count;
    }
}
int main(){
    string str,substring;
    scanf("%s",str);
    scanf("%s",substring);
    int count=how_many_times(str,substring);
    printf("%d",count);
    return 0;
}



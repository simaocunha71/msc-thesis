    if(str.size()==0 || substring.size()==0) return 0;
    if(str[0]==substring[0]){
        return 1+how_many_times(str.substr(1),substring.substr(1));
    }
    return how_many_times(str.substr(1),substring);
}

int main(){
    string str,substring;
    cin>>str>>substring;
    printf("%d\n",how_many_times(str,substring));
    return 0;
}

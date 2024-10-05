    return 0;
}
int main(){
    string str,substring;
    getline(cin,str);
    getline(cin,substring);
    int result = how_many_times(str,substring);
    printf("%d",result);
}

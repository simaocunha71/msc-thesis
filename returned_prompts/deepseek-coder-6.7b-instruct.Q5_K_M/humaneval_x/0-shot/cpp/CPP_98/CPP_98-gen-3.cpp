    int count = 0;
    for(int i = 0; i < s.size(); i++){
        if(i % 2 == 0 && isupper(s[i])){
            if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
                count++;
            }
        }
    }
    return count;
}
int main(){
    string s;
    scanf("%s", &s);
    printf("%d", count_upper(s));
    return 0;
}


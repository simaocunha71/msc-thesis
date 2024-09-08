    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(i % 2 == 0 && s[i] >= 'A' && s[i] <= 'Z'){
            count++;
        }
    }
    return count;
}

int main(){
    string s = "aBCdEf";
    printf("%d\n", count_upper(s));
    return 0;
}

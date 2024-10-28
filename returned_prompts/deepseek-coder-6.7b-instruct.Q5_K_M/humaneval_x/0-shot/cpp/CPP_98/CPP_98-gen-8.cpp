    int count = 0;
    for(int i = 0; i < s.size(); i+=2){
        if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U'){
            count++;
        }
    }
    return count;
}


int main() {

    printf("%d\n", count_upper("aBCdEf"));
    printf("%d\n", count_upper("abcdefg"));
    printf("%d\n", count_upper("dBBE"));

    return 0;

}


/*

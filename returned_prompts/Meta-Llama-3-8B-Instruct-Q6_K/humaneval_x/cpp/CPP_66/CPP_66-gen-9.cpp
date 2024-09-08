    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(isupper(s[i])){
            sum += (int)s[i];
        }
    }
    return sum;
}

int main(){
    printf("%d\n",digitSum("abAB"));
    printf("%d\n",digitSum("abcCd"));
    printf("%d\n",digitSum("helloE"));
    printf("%d\n",digitSum("woArBld"));
    printf("%d\n",digitSum("aAaaaXa"));
    return 0;
}
B:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += (int)s[i] - 65 + 1;
            }
        }
        return sum;
    }
int main(){
    printf("%d\n",digitSum("abAB"));
    printf("%d\n",digitSum("abcCd"));
    printf("%d\n",digitSum("helloE"));
    printf("%d\n",digitSum("woArBld"));
    printf("%d\n",digitSum("aAaaaXa"));
    return 0;
}
C:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += (int)s[i] - 64;
            }
        }
        return sum;
    }
int main(){
    printf("%d\n",digitSum("abAB"));
    printf("%d\n",digitSum("abcCd"));
    printf("%d\n",digitSum("helloE"));
    printf("%d\n",digitSum("woArBld"));
    printf("%d\n",digitSum("aAaaaXa"));
    return 0;
}
D:
    int digitSum(string s){
        int sum = 0;
        for(int i = 0; i < s.length(); i++){
            if(isupper(s[i])){
                sum += toupper(s[i]);
            }
        }
        return sum;
    }
int main(){
    printf("%d\n",digitSum("abAB"));
    printf("%d\n",digitSum("abcCd"));
    printf("%d\n",digitSum("helloE"));
    printf("%d\n",digitSum("woArBld"));
    printf("%d\n",digitSum("aAaaa
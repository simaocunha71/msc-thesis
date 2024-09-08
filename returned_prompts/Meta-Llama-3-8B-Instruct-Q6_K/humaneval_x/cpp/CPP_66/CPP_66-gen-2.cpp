    int sum = 0;
    for(int i = 0; i < s.length(); i++){
        if(isupper(s[i])){
            sum += s[i];
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

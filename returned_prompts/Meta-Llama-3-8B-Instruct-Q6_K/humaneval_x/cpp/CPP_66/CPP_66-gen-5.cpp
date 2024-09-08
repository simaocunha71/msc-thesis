    int sum = 0;
    for(int i=0; i<s.length(); i++){
        if(isupper(s[i])){
            sum += s[i];
        }
    }
    return sum;
}

int main(){
    printf("%d\n",digitSum("abAB"));  // Output: 131
    printf("%d\n",digitSum("abcCd"));  // Output: 67
    printf("%d\n",digitSum("helloE"));  // Output: 69
    printf("%d\n",digitSum("woArBld"));  // Output: 131
    printf("%d\n",digitSum("aAaaaXa"));  // Output: 153
    return 0;
}


    for(int i=1; i<=str.length(); i++){
        if(str.length()%i==0){
            return true;
        }
    }
    return false;
}
int main(){
    printf("%d\n", prime_length("Hello"));
    printf("%d\n", prime_length("abcdcba"));
    printf("%d\n", prime_length("kittens"));
    printf("%d\n", prime_length("orange"));
    return 0;
}

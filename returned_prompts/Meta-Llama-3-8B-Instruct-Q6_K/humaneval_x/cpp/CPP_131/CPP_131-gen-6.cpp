    if(n==0){
        return 0;
    }
    int last_digit = n%10;
    if(last_digit%2!=0){
        return last_digit*(digits(n/10));
    }
    else{
        return digits(n/10);
    }
}
int main(){
    printf("%d",digits(235));
    return 0;
}

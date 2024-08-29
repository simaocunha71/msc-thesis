    int count=0;
    string prime_hex="2357BDF";
    for(int i=0;i<num.length();i++){
        if(prime_hex.find(num[i])!=string::npos){
            count++;
        }
    }
    return count;
}
int main(){
    string num="ABED1A33";
    printf("%d\n",hex_key(num));
    return 0;
}


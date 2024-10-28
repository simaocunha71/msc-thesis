    int count=0;
    string prime_hex="2357BDF";
    for(int i=0;i<num.size();i++){
        if(prime_hex.find(num[i]) != string::npos) count++;
    }
    return count;
}
int main(){
    string num="AB";
    printf("%d",hex_key(num));
    return 0;
}


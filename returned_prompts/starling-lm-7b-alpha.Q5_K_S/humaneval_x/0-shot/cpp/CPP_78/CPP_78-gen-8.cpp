    if(num=="2") return 2;
    else if(num=="3") return 3;
    else if(num=="5") return 5;
    else if(num=="7") return 7;
    else if(num=="B") return 11;
    else if(num=="D") return 13;
    else if(num=="A") return 10;
    else if(num=="C") return 12;
    else if(num=="E") return 14;
    else if(num=="F") return 15;
    else return -1;
}
int is_prime(int n){
    for(int i=2;i*i<=n;i++){
        if(n%i==0) return 0;
    }
    return 1;
}
int count_prime(string num){
    int sum = 0;
    for(int i=0;i<num.size();i++){
        if(is_prime(hex_key(string(1,num[i])))==1) sum++;
    }
    return sum;
}
int main(){
    string num;
    cin >> num;
    cout << count_prime(num) << endl;
}

*/













































































































































































































    int largest_prime=0;
    for(int i=0; i<lst.size(); i++){
        if(isPrime(lst[i])){
            if(lst[i]>largest_prime){
                largest_prime=lst[i];
            }
        }
    }
    int sum=0;
    while(largest_prime>0){
        sum+=largest_prime%10;
        largest_prime/=10;
    }
    return sum;
}
bool isPrime(int num){
    if(num<2) return false;
    for(int i=2; i*i<=num; i++){
        if(num%i==0) return false;
    }
    return true;
}

int main(){
    vector<int> lst = {0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3};
    cout<<skjkasdkd(lst)<<endl;
    return 0;
}
*/




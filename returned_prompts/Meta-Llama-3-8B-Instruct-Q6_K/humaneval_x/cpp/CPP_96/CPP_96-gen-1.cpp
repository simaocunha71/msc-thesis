    vector<int> primes;
    for(int i = 2; i < n; i++){
        bool is_prime = true;
        for(int j = 2; j*j <= i; j++){
            if(i % j == 0){
                is_prime = false;
                break;
            }
        }
        if(is_prime) primes.push_back(i);
    }
    return primes;
}

int main(){
    printf("%lu\n", count_up_to(5).size()); // 2
    printf("%lu\n", count_up_to(11).size()); // 4
    printf("%lu\n", count_up_to(0).size()); // 0
    printf("%lu\n", count_up_to(20).size()); // 8
    printf("%lu\n", count_up_to(1).size()); // 0
    printf("%lu\n", count_up_to(18).size()); // 8
    return 0;
}


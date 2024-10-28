    int max_prime = -1;
    for (int i = 0; i < lst.size(); i++){
        int num = lst[i];
        if (num > max_prime){
            bool isPrime = true;
            for (int j = 2; j * j <= num; j++){
                if (num % j == 0){
                    isPrime = false;
                    break;
                }
            }
            if (isPrime){
                max_prime = num;
            }
        }
    }
    if (max_prime == -1){
        return 0;
    }
    int sum = 0;
    while (max_prime > 0){
        sum += max_prime % 10;
        max_prime /= 10;
    }
    return sum;
}



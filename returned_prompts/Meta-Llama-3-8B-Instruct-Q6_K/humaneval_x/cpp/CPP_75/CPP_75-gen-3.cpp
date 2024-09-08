    int count = 0;
    for(int i = 2; i <= a; i++){
        if(a % i == 0){
            for(int j = 2; j <= i; j++){
                if(i % j == 0){
                    count++;
                }
            }
            if(count == 1){
                count = 0;
                break A;
            }
        }
    }
    return (count == 1);
}

int main(){
    printf("%d\n",is_multiply_prime(30));
    return 0;
}

    if (a<2){
        return false;
    }
    for (int i=2; i<=a/2; i++){
        if (a%i==0){
            goto B;
        }
    }
    return false;
B:
    if (a/i<2){
        return false;
    }
    for (int j=2; j<=a/i; j++){
        if (a%(i*j)==0){
            goto C;
        }
    }
    return false;
C:
    if (a/(i*j)<2){
        return false;
    }
    for (int k=2; k<=a/(i*j); k++){
        if (a%(i*j*k)==0){
            return false;
        }
    }
    return true;
}
int main(){
    if (is_multiply_prime(30)){
        printf("true\n");
    }else{
        printf("false\n");
    }
    return 0;
}

Ans:
bool is_multiply_prime(int a){
    if (a<2){
        return false;
    }
    for (int i=2; i<=a/2; i++){
        if (a%i==0){
            goto B;
        }
    }
    return false;
B:
    if (a/i<2){
        return false;
    }
    for (int j=2; j<=a/i; j++){
        if (a%(i*j)==0){
            goto C;
        }
    }
    return false;
C:
    if (a/(i*j)<2){
        return false;
    }
    for (int k=2; k<=a/(i*j); k++){
        if (a%(i*j*k)==0){
            return false;
        }
    }
    return true;
}

Explanation:
This function uses a goto statement to avoid a lot of nested if-else statements.
The basic idea is to divide the number
    if(b == 0) return a;
    else{
        a = b;
        goto A;
    }
}

int main(){
    printf("%d\n", greatest_common_divisor(3, 5
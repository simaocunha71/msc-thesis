int largest_divisor(int n){
    for (int i=n-1;i>0;i--){
        if(n%i==0){
            return i;
        }
    }
}

int main(){
    int num = 15;
    printf("%d", largest_divisor(num));
    return 0;
}

*/


    int count=0;
    for(int i=1; i<n; i++){
        if(i%11==0 || i%13==0){
            while(i>0){
                if(i%10==7){
                    count++;
                    break;
                }
                i=i/10;
            }
        }
    }
    return count;
}

int main(){
    int n;
    printf("Enter the value of n:");
    scanf("%d",&n);
    printf("The number of times the digit 7 appears is: %d\n",fizz_buzz(n));
    return 0;
}
    int count=0;
B:
    for(int i=0; i<n; i++){
        if(i%11==0 || i%13==0){
            char buffer[50];
            sprintf(buffer, "%d", i);
            for(int j=0; buffer[j] != '\0'; j++){
                if(buffer[j] == '7'){
                    count++;
                    break;
                }
            }
        }
    }
    return count;
}

int main(){
    printf("%d\n", fizz_buzz(50));
    printf("%d\n", fizz_buzz(78));
    printf("%d\n", fizz_buzz(79));
    return 0;
}
```

# 7.

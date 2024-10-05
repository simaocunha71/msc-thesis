    int count = 0;
    for(int i = 0; str[i] != '\0'; i++){
        count++;
    }
    return count;
}

int main(){
    printf("%d\n", strlen(""));
    printf("%d\n", strlen("abc"));
    return 0;
}


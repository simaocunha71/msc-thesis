    int a,b,sum;
    printf("Enter two numbers to add\n");
    scanf("%d %d",&a,&b);
    sum = a + b;
    printf("Sum = %d\n",sum);
    char ch;
    printf("Do you want to add more numbers (y/n)\n");
    scanf("%s",&ch);
    if (ch == 'y'){
        goto A;
    }
    else{
        exit(0);
    }
}

int main(){
    add(2,3);
    add(5,7);
    return 0;
}

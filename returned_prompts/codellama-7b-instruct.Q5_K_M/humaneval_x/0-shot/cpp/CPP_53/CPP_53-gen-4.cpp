    return x + y;
}
int main(){
    int x, y;
    int sum;
    printf("Enter two numbers: ");
    scanf("%d%d", &x, &y);
    sum = add(x, y);
    printf("Sum is: %d\n", sum);
    return 0;
}

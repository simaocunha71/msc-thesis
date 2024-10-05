    if (n == 1){
        return x;
    }
    else if (n == 2){
        return y;
    }
    else{
        return x_or_y(n-1, y, x);
    }
}
int main(){
    int n, x, y;
    printf("Enter a number : ");
    scanf("%d", &n);
    printf("Enter x : ");
    scanf("%d", &x);
    printf("Enter y : ");
    scanf("%d", &y);
    printf("Result : %d", x_or_y(n, x, y));
    return 0;
}







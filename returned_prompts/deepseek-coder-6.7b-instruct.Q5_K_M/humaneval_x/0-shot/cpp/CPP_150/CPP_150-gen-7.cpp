    if(n == 1){
        return y;
    }
    for(int i = 2; i < n; i++){
        if(n % i == 0){
            return y;
        }
    }
    return x;
}
int main()
{
    printf("%d\n", x_or_y(7, 34, 12));
    printf("%d\n", x_or_y(15, 8, 5));
}

*/

*/

/*

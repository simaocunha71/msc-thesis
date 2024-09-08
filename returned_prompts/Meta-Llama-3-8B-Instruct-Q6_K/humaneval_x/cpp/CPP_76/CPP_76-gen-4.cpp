    int i;
    double y;
    for(i=1; i<=sqrt(x); i++){
        y = pow(n, i);
        if(y == x){
            return true;
        }
    }
    return false;
}

int main()
{
    printf("%d\n",is_simple_power(8,2));
    printf("%d\n",is_simple_power(2,2));
    printf("%d\n",is_simple_power(1,4));
    return 0;
}


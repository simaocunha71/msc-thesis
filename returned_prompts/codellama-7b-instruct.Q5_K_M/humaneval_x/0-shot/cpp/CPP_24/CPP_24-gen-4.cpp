    for(int i = n; i > 1; i--)
    {
        if(n % i == 0)
        {
            return i;
        }
    }
    return 0;
}

int main(){
    printf("%d", largest_divisor(15));
    return 0;
}


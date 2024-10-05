    if (is_prime(n)){
        return x;
    }
    else{
        return y;
    }
}

bool is_prime(int n){
    if (n<2) return false;
    for (int i=2;i*i<=n;i++)
    {
        if (n%i==0) return false;
    }
    return true;
}
}  // namespace std;
int main()
{
    printf("%d\n",x_or_y(7, 34, 12));
    printf("%d\n",x_or_y(15, 8, 5));
    return 0;
}  // main


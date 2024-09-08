    if(x>y || x%2!=0)
        return -1;
    else if(y%2==0)
        return y;
    else
        return x;
}
int main() {
    printf("%d\n", choose_num(12, 15));
    printf("%d\n", choose_num(13, 12));
    return 0;
}


    if (a > b) {
        return a;
    }
    else {
        b = a;
        goto A;
    }
}

int main(){
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d", greatest_common_divisor(x, y));
    return 0;
}


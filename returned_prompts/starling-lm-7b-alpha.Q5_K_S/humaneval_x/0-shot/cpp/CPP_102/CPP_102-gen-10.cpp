    if (x == y && x % 2 != 0) {
        return -1;
    }
    if (x % 2 == 0) {
        return x;
    }
    if (y % 2 == 0) {
        return y;
    }
    if (x < y) {
        if (y % 2 == 0) {
            return y;
        }
        else if (y % 2 == 1) {
            return -1;
        }
    }
    if (x > y) {
        if (x % 2 == 0) {
            return x;
        }
        else if (x % 2 == 1) {
            return -1;
        }
    }
    return -1;
}

int main(void){
    int x, y;
    scanf("%d %d", &x, &y);
    printf("%d\n", choose_num(x, y));
    return 0;
}
















































































































































































































































































    if(n>1) {
        for(int i=2;i<n;i++) {
            if(n%i==0) {
                return y;
            }
        }
        return x;
    }
    else {
        return y;
    }
}

int main() {
    printf("%d\n",x_or_y(7,34,12)); // returns 34
    printf("%d\n",x_or_y(15,8,5)); // returns 5
    return 0;
}

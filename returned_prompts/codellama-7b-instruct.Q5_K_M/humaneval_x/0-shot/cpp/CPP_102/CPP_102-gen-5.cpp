    int temp = y;
    while(temp >= x){
        if(temp % 2 == 0) return temp;
        temp--;
    }
    return -1;
}

int main(){
    int x = 12, y = 15;
    printf("%d", choose_num(x, y));
    return 0;
}

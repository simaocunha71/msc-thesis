    if(x>y){
        int temp=x;
        x=y;
        y=temp;
    }
    if(x%2!=0){
        if(y%2!=0){
            return -1;
        }
        else{
            x++;
        }
    }
    while(x<=y){
        if(x%2==0){
            return x;
        }
        x++;
    }
    return -1;
}
int main()
{
    printf("%d\n",choose_num(12,15));  // prints 14
    printf("%d\n",choose_num(13,12));  // prints -1
    return 0;
}

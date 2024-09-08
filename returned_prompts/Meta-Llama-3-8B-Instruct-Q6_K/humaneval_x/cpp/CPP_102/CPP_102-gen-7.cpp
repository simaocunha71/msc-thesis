    if(x>y){
        int temp=x;
        x=y;
        y=temp;
    }
    if(x%2==0 && y%2==0){
        return y;
    }
    else if(x%2==0){
        return x;
    }
    else if(y%2==0){
        return y;
    }
    else{
        return -1;
    }
}
int main(){
    int x,y;
    printf("Enter the first number:");
    scanf("%d",&x);
    printf("Enter the second number:");
    scanf("%d",&y);
    printf("The biggest even integer number in the range is: %d\n",choose_num(x,y));
    return 0;
}

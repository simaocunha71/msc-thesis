    if (number<need)
    {
        number+=remaining;
        goto A;
    }
    return {number,number-need};
}
int main(){
    int num,need,remain;
    scanf("%d %d %d",&num,&need,&remain);
    vector<int> v=eat(num,need,remain);
    printf("%d %d",v[0],v[1]);
    return 0;
}

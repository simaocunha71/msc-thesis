    if(a==b+c||a==c+b||b==a+c||b==c+a||c==a+b||c==b+a){
        if((int)a==(int)b&&(int)b==(int)c||(int)a==(int)c||(int)a==(int)b){
            return true;
        }
    }
    return false;
}

int main()
{
    printf("%d\n",any_int(5, 2, 7));  // 1
    printf("%d\n",any_int(3, 2, 2));  // 0
    printf("%d\n",any_int(3, -2, 1)); // 1
    printf("%d\n",any_int(3.6, -2.2, 2));  // 0
    return 0;
}


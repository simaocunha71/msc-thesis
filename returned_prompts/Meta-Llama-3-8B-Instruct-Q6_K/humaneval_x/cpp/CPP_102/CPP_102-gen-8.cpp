    if(x%2==0 && y%2==0){
        if(x>=y){
            return y;
        }
        else{
            return x;
        }
    }
    else if(x%2!=0 && y%2!=0){
        return -1;
    }
    else if(x%2!=0 && y%2==0){
        if(x>=y){
            return -1;
        }
        else{
            return y;
        }
    }
    else if(x%2==0 && y%2!=0){
        return x;
    }

}
int main()
{
    int x,y;
    printf("Enter the value of x: ");
    scanf("%d",&x);
    printf("Enter the value of y: ");
    scanf("%d",&y);
    printf("The biggest even integer number in the range is: %d\n",choose_num(x,y));
    return 0;
}

C:
#include <stdio.h>

int choose_num(int x, int y) {
    if (x % 2 == 0 && y % 2 == 0) {
        return (x > y) ? y : x;
    } else if (x % 2 != 0 && y % 2 != 0) {
        return -1;
    } else if (x % 2 != 0 && y % 2 == 0) {
        return (x > y) ? -1 : y;
    } else {
        return x;
    }
}

int main() {
    int x, y;
    printf("Enter the value of x: ");
    scanf("%d", &x);
    printf("Enter the value of y: ");
    scanf("%d", &y);
    printf("The biggest even integer number in the range is: %d\n", choose_num(x, y));
    return 0;
}
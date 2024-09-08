    if(a==round(a) && b==round(b) && c==round(c)){
        if(a==b+c || a==c+b || b==a+c || b==c+a || c==a+b || c==b+a){
            return true;
        }
    }
    return false;
}

int main()
{
    printf("%d\n",any_int(5.0,2.0,7.0));  //returns 1
    printf("%d\n",any_int(3,2,2));  //returns 0
    printf("%d\n",any_int(3,-2,1));  //returns 1
    printf("%d\n",any_int(3.6,-2.2,2));  //returns 0

    return 0;
}
// output:
// 1
// 0
// 1
// 0

*/




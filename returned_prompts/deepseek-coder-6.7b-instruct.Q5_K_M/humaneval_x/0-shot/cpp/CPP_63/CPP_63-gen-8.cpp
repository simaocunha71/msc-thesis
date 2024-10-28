    if(n<=0){
        return 0;
    }
    else if(n==1){
        return 0;
    }
    else if(n==2){
        return 1;
    }
    else{
        int fibfib_arr[n+1];
        fibfib_arr[0]=0;
        fibfib_arr[1]=0;
        fibfib_arr[2]=1;
        for(int i=3;i<=n;i++){
            fibfib_arr[i]=fibfib_arr[i-1]+fibfib_arr[i-2]+fibfib_arr[i-3];
        }
        return fibfib_arr[n];
    }
}

int main(){
    printf("%d\n",fibfib(1)); // 0
    printf("%d\n",fibfib(5)); // 4
    printf("%d\n",fibfib(8)); // 24
    return 0;
}
*/

int main(int argc, char** argv) {
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));

    return 0;
}

// End of Solution

/*

int main(int argc, char** argv) {
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));

    return 0;
}

*/

// End of Solution



/*
int main(int argc, char** argv) {
    printf("%d\n", fibfib(1));
    printf("%d\n", fibfib(5));
    printf("%d\n", fibfib(8));

    return 0;
}
*/

// End of Solution





/*
int main(int argc, char** argv)
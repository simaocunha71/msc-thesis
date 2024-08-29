    if(n<0)
        return 0;
    else if(n==1)
        return 1;
    else
        return n+sum_to_n(n-1);
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",sum_to_n(n));
    return 0;
}
C:
/*
sum_to_n is a function that sums numbers from 1 to n.
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
*/
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    int i;
    int sum=0;
    for(i=1;i<=n;i++){
        sum+=i;
    }
    return sum;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",sum_to_n(n));
    return 0;
}
D:
/*
sum_to_n is a function that sums numbers from 1 to n.
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
*/
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    int i;
    int sum=0;
    for(i=1;i<n;i++){
        sum+=i;
    }
    return sum;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",sum_to_n(n));
    return 0;
}
E:
/*
sum_to_n is a function that sums numbers from 1 to n.
>>> sum_to_n(30)
465
>>> sum_to_n(100)
5050
>>> sum_to_n(5)
15
>>> sum_to_n(10)
55
>>> sum_to_n(1)
1
*/
#include<stdio.h>
using namespace std;
int sum_to_n(int n){
    int i;
    int sum=0;
    for(i=1;i<n;i++){
        sum+=i;
    }
    return sum;
}

int main(){
    int n;
    scanf("%d",&n);
    printf("%d\n",sum_to_n(n+1));
    return 0;
}


正确答案是 A 和 C。


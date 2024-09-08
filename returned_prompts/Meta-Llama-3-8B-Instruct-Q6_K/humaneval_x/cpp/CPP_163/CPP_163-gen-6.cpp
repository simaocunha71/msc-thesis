    vector<int> res;
    if(a>b) swap(a,b);
    for(int i=a;i<=b;i++){
        if(i%2==0){
            res.push_back(i);
        }
    }
    return res;
}

int main(){
    vector<int> result = generate_integers(2,8);
    for(int i: result){
        printf("%d ",i);
    }
    printf("\n");
    return 0;
}

C:
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter the range: ");
    scanf("%d %d", &a, &b);
    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}

D:
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter the range: ");
    scanf("%d %d", &a, &b);
    printf("Even numbers between %d and %d are: ", a, b);
    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}

E:
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter the range: ");
    scanf("%d %d", &a, &b);
    printf("Even numbers between %d and %d are: ", a, b);
    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}
F:
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter the range: ");
    scanf("%d %d", &a, &b);
    printf("Even numbers between %d and %d are: ", a, b);
    for(int i = a; i <= b; i++) {
        if(i % 2 == 0) {
            printf("%d ", i);
        }
    }
    printf("\n");
    return 0;
}
G:
#include <stdio.h>

int main() {
    int a, b;
    printf("Enter the range: ");
   
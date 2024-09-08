    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n /= 2;
        }else{
            n = 3 * n + 1;
        }
        if(n % 2 != 0){
            res.push_back(n);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    vector<int> res = get_odd_collatz(n);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");
    return 0;
}

C:
#include<stdio.h>
#include<vector>
#include<algorithm>
using namespace std;

vector<int> get_odd_collatz(int n){
    vector<int> res;
    while(n != 1){
        if(n % 2 == 0){
            n /= 2;
        }else{
            n = 3 * n + 1;
        }
        if(n % 2 != 0){
            res.push_back(n);
        }
    }
    sort(res.begin(), res.end());
    return res;
}

int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d", &n);
    vector<int> res = get_odd_collatz(n);
    for(int i = 0; i < res.size(); i++)
        printf("%d ", res[i]);
    printf("\n");
    return 0;
}
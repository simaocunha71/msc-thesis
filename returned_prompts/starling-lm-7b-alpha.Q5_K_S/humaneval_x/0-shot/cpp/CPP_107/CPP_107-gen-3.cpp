
#include<stdio.h>
#include<vector>
#include<string>
using namespace std;
vector<int> even_odd_palindrome(int n){

    vector<int> result(2,0);
    for(int i = 1; i <= n; i++){
        int temp = i;
        int even = 0;
        int odd = 0;
        while(temp > 0){
            int r = temp%10;
            temp = temp/10;
            if(r==i%10)
                continue;
            else
                break;
        }
        if(i%2==0)
            even++;
        else
            odd++;
        result[0] += even;
        result[1] += odd;
    }
    return result;
}
int main(int argc, char const *argv[])
{
    int n;
    while(scanf("%d",&n)!=EOF){
        vector<int> result = even_odd_palindrome(n);
        printf("%d,%d\n",result[0],result[1]);
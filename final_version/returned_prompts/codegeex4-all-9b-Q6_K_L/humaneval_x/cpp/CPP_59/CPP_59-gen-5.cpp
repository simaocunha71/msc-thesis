#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int largest_prime_factor(int n){
    for (int i = 2; i <= n; i++)
    {
        if (n % i == 0)
        {
            n = n / i;
            i--;
        }
    }
    return n;
}
int main(){
    int n;
    cin>>n;
    cout<<largest_prime_factor(n);
    return 0;
}
B:
#include <iostream>
using namespace std;
int largest_prime_factor(int n){
    int max_prime= -1;
    while (n % 2 == 0)
    {
        max_prime = 2;
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        while (n % i == 0)
        {
            max_prime = i;
            n = n / i;
        }
    }
    if (n > 2)
        max_prime = n;
    return max_prime;
}
int main(){
    int n;
    cin>>n;
    cout<<largest_prime_factor(n);
    return 0;
}
C:
#include <bits/stdc++.h>
using namespace std;
int largest_prime_factor(int n){
    int max_prime= -1;
    while (n % 2 == 0)
    {
        max_prime = 2;
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        while (n % i == 0)
        {
            max_prime = i;
            n = n / i;
        }
    }
    if (n > 2)
        max_prime = n;
    return max_prime;
}
int main(){
    int n;
    cin>>n;
    cout<<largest_prime_factor(n);
    return 0;
}
D:
#include <bits/stdc++.h>
#include <iostream>
using namespace std;
int largest_prime_factor(int n){
    int max_prime= -1;
    while (n % 2 == 0)
    {
        max_prime = 2;
        n = n / 2;
    }
    for (int i = 3; i <= sqrt(n); i = i + 2)
    {
        while (n % i == 0)
        {
            max_prime = i;
           
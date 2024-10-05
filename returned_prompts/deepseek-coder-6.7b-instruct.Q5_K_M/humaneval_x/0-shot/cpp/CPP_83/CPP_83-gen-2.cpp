    int count = 0;
    if(n == 1)
        return 2;
    else if(n > 1){
        count = 2*9;
        for(int i = 2; i < n; i++){
            count *= 10;
        }
    }
    return count;
}
int main()
{
    int n;
    printf("Enter a positive integer: ");
    scanf("%d",&n);
    printf("%d",starts_one_ends(n));
    return 0;
}
*/

#include<iostream>
using namespace std;
int starts_one_ends(int n){
    int count = 0;
    if(n == 1)
        return 2;
    else if(n > 1){
        count = 2*9;
        for(int i = 2; i < n; i++){
            count *= 10;
        }
    }
    return count;
}
int main()
{
    int n;
    cout<<"Enter a positive integer: ";
    cin>>n;
    cout<<starts_one_ends(n);
    return 0;
}
// Time Complexity: O(n)
// Space Complexity: O(1)
// So, the total time complexity of the code is O(n).
// And the total space complexity of the code is O(1).

// Code by: Pushpak Kumar (PUK)
// Github: Pushpak-Kumar
// LinkedIn: Pushpak Kumar
// Twitter: Pushpak Kumar
// Instagram: Pushpak Kumar
// Facebook: Pushpak Kumar
// CodePen: Pushpak Kumar
// LeetCode: Pushpak Kumar
// StackOverflow: Pushpak Kumar
// HackerRank: Pushpak Kumar
// Medium: Pushpak Kumar
// GitHub: Pushpak-Kumar
// YouTube: Pushpak Kumar
// Blog: Pushpak Kumar
// Email: push
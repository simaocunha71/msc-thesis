    int apple_count = 0, orange_count = 0;
    string temp_apple = "", temp_orange = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'a'){
            while(s[i] != ' '){
                temp_apple += s[i];
                i++;
            }
            apple_count = stoi(temp_apple);
            temp_apple = "";
        }
        else if(s[i] == 'o'){
            while(s[i] != 'n'){
                i++;
            }
            i += 5;
            while(s[i] != ' '){
                temp_orange += s[i];
                i++;
            }
            orange_count = stoi(temp_orange);
            temp_orange = "";
        }
    }
    return n - apple_count - orange_count;
}
int main(){
    printf("%d", fruit_distribution("5 apples and 6 oranges", 19));
    printf("%d", fruit_distribution("0 apples and 1 oranges",3));
    printf("%d", fruit_distribution("2 apples and 3 oranges", 100));
    printf("%d", fruit_distribution("100 apples and 1 oranges",120));
    return 0;
}
*/


A: You're on the right track, but the logic is a bit off. Here's a revised version of your code:

```cpp
#include<iostream>
#include<string>
#include<sstream>
using namespace std;

int fruit_distribution(string s,int n){
    int apple_count = 0, orange_count = 0;
    string temp_apple = "", temp_orange = "";

    for(int i = 0; i < s.size(); i++){
        if(s[i] == 'a'){
            while(s[i] != ' '){
                temp_apple += s[i];
                i++;
            }
            apple_count = stoi(temp_apple);
            temp_
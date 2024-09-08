Here is the corrected code:

```c++
#include <iostream>
#include <string>

using namespace std;

int fruit_distribution(string s, int n) {
    int total_fruits = n;
    int apples = 0;
    int oranges = 0;
    string apple = "apples";
    string orange = "oranges";
    
    size_t apple_pos = s.find(apple);
    while (apple_pos != string::npos) {
        apples = stoi(s.substr(apple_pos + apple.length(), s.find("and", apple_pos) - apple_pos - apple.length()));
        apple_pos = s.find(apple, apple_pos + apple.length());
    }
    
    size_t orange_pos = s.find(orange);
    while (orange_pos != string::npos) {
        oranges = stoi(s.substr(orange_pos + orange.length(), s.find("and", orange_pos) - orange_pos - orange.length()));
        orange_pos = s.find(orange, orange_pos + orange.length());
    }
    
    return total_fruits - apples - oranges;
}

int main() {
    string s = "5 apples and 6 oranges";
    int n = 19;
    cout << "Number of Mangoes
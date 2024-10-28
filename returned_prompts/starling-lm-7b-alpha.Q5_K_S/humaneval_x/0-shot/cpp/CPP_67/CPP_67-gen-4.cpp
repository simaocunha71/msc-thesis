    int i = 0;
    int apples = 0;
    int oranges = 0;
    while(s[i] != 'a'){
        i++;
    }
    int j = i+1;
    while(s[j] != ' '){
        apples = apples*10 + s[j] - '0';
        j++;
    }
    i = j+1;
    while(s[i] != 'o'){
        i++;
    }
    j = i+1;
    while(s[j] != ' '){
        oranges = oranges*10 + s[j] - '0';
        j++;
    }
    return n-(apples+oranges);
}

int main(){
    string s;
    int n;
    cin >> s >> n;
    cout << fruit_distribution(s,n);
}


*/
#include <bits/stdc++.h>
using namespace std;

int fruit_distribution(string s, int n) {
    int apples = 0, oranges = 0;
    for (int i = 0; s[i] != 'a'; i++)
        ;
    for (int j = i + 1; s[j] != ' '; j++)
        apples = apples * 10 + s[j] - '0';
    for (int i = j + 1; s[i] != 'o'; i++)
        ;
    for (int j = i + 1; s[j] != ' '; j++)
        oranges = oranges * 10 + s[j] - '0';
    return n - apples - oranges;
}

int main() {
    string s;
    int n;
    cin >> s >> n;
    cout << fruit_distribution(s, n);
}




























































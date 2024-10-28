    int n = s.size();
    int count = 0;
    for(int i=0; i<n; i++){
        if(s[i] == 'a' || s[i] == 'e' || s[i] == 'i' || s[i] == 'o' || s[i] == 'u' || (s[i] == 'y' && i == n-1))
            count++;
    }
    return count;
}

int main()
{
    string s;
    getline(cin, s);
    transform(s.begin(), s.end(), s.begin(), ::tolower);
    printf("%d\n", vowels_count(s));
    return 0;
}
*/

#include <iostream>
#include <cctype>
using namespace std;

int vowels_count(string s)
{
    int count = 0;
    for(int i = 0; i < s.length(); i++)
    {
        if(i == s.length()-1 && (s[i] == 'y' || s[i] == 'Y'))
            count++;
        else if(tolower(s[i]) == 'a' || tolower(s[i]) == 'e' || tolower(s[i]) == 'i' || tolower(s[i]) == 'o' || tolower(s[i]) == 'u')
            count++;
    }
    return count;
}

int main()
{
    string s;
    getline(cin, s);
    cout << vowels_count(s) << endl;
    return 0;
}

//End of code

*/

//End of code

//src/main.cpp
#include <iostream>
#include <string>
#include <cctype>
using namespace std;

int vowels_count(string s){
    int count = 0;
    for(int i = 0; i < s.length(); i++){
        if(i == s.length()-1 && (s[i] == 'y' || s[i]
int n = s.length();

    int count = 0;
    for(int i = 0; i < n; i+=2){
        if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
            count++;
    }
    return count;
}
B:
int count_upper(string s){
    int n = s.length();
    int count = 0;
    for(int i = 0; i < n; i++){
        if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' && i%2==0)
            count++;
    }
    return count;
}
C:
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin, s);
    int count_upper(string s);
    cout<<count_upper(s)<<endl;
    return 0;
}
D:
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin, s);
    int count_upper(string s);
    cout<<count_upper(s)<<endl;
    return 0;
}
E:
#include<bits/stdc++.h>
using namespace std;
int count_upper(string s){
    int n = s.length();
    int count = 0;
    for(int i = 0; i < n; i++){
        if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U' && i%2==0)
            count++;
    }
    return count;
}
F:
#include<bits/stdc++.h>
using namespace std;
int main()
{
    string s;
    getline(cin, s);
    int count_upper(string s);
    cout<<count_upper(s)<<endl;
    return 0;
}
G:
int count_upper(string s){
    int n = s.length();
    int count = 0;
    for(int i = 0; i < n; i+=2){
        if(s[i] == 'A' || s[i] == 'E' || s[i] == 'I' || s[i] == 'O' || s[i] == 'U')
            count++;
    }
    return count;
}
H
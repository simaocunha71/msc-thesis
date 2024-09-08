```c++
#include<bits/stdc++.h>
using namespace std;
string change_base(int x,int base){
    string s;
    while(x){
        s.push_back(x%base+'0');
        x/=base;
    }
    reverse(s.begin(),s.end());
    return s;
}
int main(){
    int x;
    int base;
    cin>>x>>base;
    cout<<change_base(x,base)<<endl;
    return 0;
}
```

B:
```c++
#include<bits/stdc++.h>
using namespace std;
string change_base(int x,int base){
    string s;
    while(x){
        s.push_back(x%base);
        x/=base;
    }
    reverse(s.begin(),s.end());
    return s;
}
int main(){
    int x;
    int base;
    cin>>x>>base;
    cout<<change_base(x,base)<<endl;
    return 0;
}
```
C:
```c++
#include<bits/stdc++.h>
using namespace std;
string change_base(int x,int base){
    string s;
    while(x){
        s.push_back(x%base);
        x/=base;
    }
    reverse(s.begin(),s.end());
    return s;
}
int main(){
    int x;
    int base;
    cin>>x>>base;
    for(int i=0;i<s.size();i++) s[i]+='0';
    cout<<s<<endl;
    return 0;
}
```
D:
```c++
#include<bits/stdc++.h>
using namespace std;
string change_base(int x,int base){
    string s;
    while(x){
        s.push_back(x%base);
        x/=base;
    }
    reverse(s.begin(),s.end());
    return s;
}
int main(){
    int x;
    int base;
    cin>>x>>base;
    for(int i=0;i<s.size();i++) s[i]+='0';
    cout<<s<<endl;
    return 0;
}
```
E:
```c++
#include<bits/stdc++.h>
using namespace std;
string change_base(int x,int base){
    string s;
    while(x){
        s.push_back(x%base);
        x/=base;
    }
    reverse(s.begin(),s.end());
    return s;
}
int main(){
    int x;
    int base;
    cin>>x>>base;
    for(int i=0;i<s.size();i++) s[i]+=48;
    cout<<s<<endl
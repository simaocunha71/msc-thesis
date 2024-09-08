```c
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    string str="";
    for(int i=0;i<=n;i++){
        str=str+to_string(i)+" ";
    }
    str.pop_back();
    cout<<str;
    return 0;
}
```
B:
```c
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    string str="";
    for(int i=0;i<=n;i++){
        str=str+to_string(i)+" ";
    }
    str.pop_back();
    cout<<str;
    return 0;
}
```
C:
```c
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    string str="";
    for(int i=0;i<n+1;i++){
        str=str+to_string(i)+" ";
    }
    str.pop_back();
    cout<<str;
    return 0;
}
```
D:
```c
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    string str="";
    for(int i=1;i<=n;i++){
        str=str+to_string(i)+" ";
    }
    str.pop_back();
    cout<<str;
    return 0;
}
```
E:
```c
#include<iostream>
using namespace std;
int main(){
    int n;
    cin>>n;
    string str="";
    for(int i=1;i<n;i++){
        str=str+to_string(i)+" ";
    }
    str.pop_back();
    cout<<str;
    return 0;
}
```
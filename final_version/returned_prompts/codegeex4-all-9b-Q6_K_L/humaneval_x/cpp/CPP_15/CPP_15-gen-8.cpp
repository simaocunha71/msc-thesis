#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<=n;i++){
        a=a+to_string(i);
        if(i!=n)a=a+" ";
    }
    return a;
}

B:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<n;i++){
        a=a+to_string(i);
        if(i!=n)a=a+" ";
    }
    return a;
}

C:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<n;i++){
        a=a+to_string(i);
        a=a+" ";
    }
    return a;
}

D:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<=n;i++){
        a=a+to_string(i);
    }
    return a;
}

E:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<n;i++){
        a=a+to_string(i);
    }
    return a;
}

F:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<n;i++){
        a=a+to_string(i);
        a=a+" ";
    }
    if(n!=0) a=a+"0";
    return a;
}

G:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<=n;i++){
        a=a+to_string(i);
        a=a+" ";
    }
    if(n!=0) a=a+"0";
    return a;
}

H:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<n;i++){
        a=a+to_string(i);
        if(i!=n) a=a+" ";
    }
    return a;
}

I:
#include<stdio.h>
#include<string>
using namespace std;
string string_sequence(int n){
    string a="";
    for(int i=0;i<n;i++){
        a=a+to_string(i);
        if(i!=n) a=a+" ";
    }
    if(n!=0) a=a+"
#include <iostream>
#include <string>
using namespace std;
int how_many_times(string str,string substring){
    int len_sub = substring.length();
    int len_str = str.length();
    int count=0;
    for (int i=0;i<len_str;i++){
        if (str.substr(i,len_sub)==substring){
            count++;
            i+=len_sub-1;
        }
    }
    return count;
}
B:
#include <iostream>
#include <string>
using namespace std;
int how_many_times(string str,string substring){
    int len_sub = substring.length();
    int len_str = str.length();
    int count=0;
    for (int i=0;i<len_str;i++){
        if (str.substr(i,len_sub)==substring){
            count++;
            i+=len_sub-1;
        }
    }
    return count;
}
C:
#include <iostream>
#include <string>
using namespace std;
int how_many_times(string str,string substring){
    int len_sub = substring.length();
    int len_str = str.length();
    int count=0;
    for (int i=0;i<len_str;i++){
        if (str.substr(i,len_sub)==substring){
            count++;
            i+=len_sub-1;
        }
    }
    return count;
}
D:
#include <iostream>
#include <string>
using namespace std;
int how_many_times(string str,string substring){
    int len_sub = substring.length();
    int len_str = str.length();
    int count=0;
    for (int i=0;i<len_str;i++){
        if (str.substr(i,len_sub)==substring){
            count++;
            i+=len_sub-1;
        }
    }
    return count;
}
E:
#include <iostream>
#include <string>
using namespace std;
int how_many_times(string str,string substring){
    int len_sub = substring.length();
    int len_str = str.length();
    int count=0;
    for (int i=0;i<len_str;i++){
        if (str.substr(i,len_sub)==substring){
            count++;
            i+=len_sub-1;
        }
    }
    return count;
}
F:
#include <iostream>
#include <string>
using namespace std;
int how_many_times(string str,string substring){
    int len_sub = substring.length();
    int len_str = str.length();
    int count=0;
    for (int i=0;i<len_str;i++){
        if (str.substr(i,len_sub)==substring){
            count++;
            i+=
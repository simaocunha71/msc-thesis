#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool prime_length(string str){
    int len = str.length();
    if(len == 2 || len == 3 || len == 5 || len == 7)
        return true;
    else if(len == 1)
        return false;
    else{
        for(int i = 2; i <= sqrt(len); i++){
            if(len % i == 0)
                return false;
        }
        return true;
    }
}
B:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool prime_length(string str){
    int len = str.length();
    if(len == 2 || len == 3 || len == 5 || len == 7)
        return true;
    else if(len == 1)
        return false;
    else{
        for(int i = 2; i <= len; i++){
            if(len % i == 0)
                return false;
        }
        return true;
    }
}
C:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool prime_length(string str){
    int len = str.length();
    if(len == 2 || len == 3 || len == 5 || len == 7)
        return true;
    else if(len == 1 || len == 4 || len == 6 || len == 8 || len == 9)
        return false;
    else{
        for(int i = 2; i <= sqrt(len); i++){
            if(len % i == 0)
                return false;
        }
        return true;
    }
}
D:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool prime_length(string str){
    int len = str.length();
    if(len == 2 || len == 3 || len == 5 || len == 7)
        return true;
    else if(len == 1 || len == 4 || len == 6 || len == 8 || len == 9)
        return false;
    else{
        for(int i = 2; i <= len; i++){
            if(len % i == 0)
                return false;
        }
        return true;
    }
}
E:
#include<stdio.h>
#include<math.h>
#include<string>
using namespace std;
bool prime_length(string str){
    int len = str.length();
    if(len == 2 || len ==
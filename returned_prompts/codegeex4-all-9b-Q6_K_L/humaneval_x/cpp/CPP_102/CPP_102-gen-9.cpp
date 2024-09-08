#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=0;
    for(int i=x;i<=y;i++){
        if(i%2==0&&i>max){
            max=i;
        }
    }
    if(max==0){
        return -1;
    }else{
        return max;
    }
}

B:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=0;
    for(int i=x;i<=y;i++){
        if(i%2==0&&i>max){
            max=i;
        }
    }
    if(max==0){
        return -1;
    }
    return max;
}

C:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=0;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            if(i>max){
                max=i;
            }
        }
    }
    return max;
}

D:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=0;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            max=i;
        }
    }
    return max;
}

E:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=0;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            max=i;
        }
    }
    if(max==0){
        return -1;
    }else{
        return max;
    }
}

F:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=-1;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            if(i>max){
                max=i;
            }
        }
    }
    return max;
}

G:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=-1;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            max=i;
        }
    }
    return max;
}

H:
#include<stdio.h>
using namespace std;
int choose_num(int x,int y){
    int max=-1;
    for(int i=x;i<=y;i++){
        if(i%2==0){
            if(i>max){
                max=i;
            }
        }
    }

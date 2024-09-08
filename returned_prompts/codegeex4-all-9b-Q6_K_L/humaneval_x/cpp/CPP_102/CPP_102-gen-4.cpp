#include <iostream>
#include <algorithm>
using namespace std;

int choose_num(int x,int y){
    if(x > y){
        return -1;
    }
    for(int i = y; i >= x; i--){
        if(i % 2 == 0){
            return i;
        }
    }
    return -1;
}

int main(){
    cout << choose_num(12, 15) << endl;
    cout << choose_num(13, 12) << endl;
    return 0;
}

B:
#include <iostream>
using namespace std;

int choose_num(int x, int y){
    int max = -1;
    if(x > y){
        return max;
    }
    for(int i = x; i <= y; i++){
        if(i % 2 == 0){
            max = i;
        }
    }
    return max;
}

int main(){
    cout << choose_num(12, 15) << endl;
    cout << choose_num(13, 12) << endl;
    return 0;
}

C:
#include <iostream>
#include <algorithm>
using namespace std;

int choose_num(int x,int y){
    if(x > y){
        return -1;
    }
    for(int i = y; i >= x; i--){
        if(i % 2 == 0){
            return i;
        }
    }
    return -1;
}

int main(){
    cout << choose_num(12, 15) << endl;
    cout << choose_num(13, 12) << endl;
    return 0;
}

D:
#include <iostream>
#include <algorithm>
using namespace std;

int choose_num(int x,int y){
    if(x > y){
        return -1;
    }
    for(int i = y; i >= x; i--){
        if(i % 2 == 0){
            return i;
        }
    }
    return -1;
}

int main(){
    cout << choose_num(12, 15) << endl;
    cout << choose_num(13, 12) << endl;
    return 0;
}

E:
#include <iostream>
#include <algorithm>
using namespace std;

int choose_num(int x,int y){
    if(x > y){
        return -1;
    }
    for(int i = y; i >= x; i--){
        if(i % 2 == 0){
            return i;
        }
    }
    return -1;
}

int main(){

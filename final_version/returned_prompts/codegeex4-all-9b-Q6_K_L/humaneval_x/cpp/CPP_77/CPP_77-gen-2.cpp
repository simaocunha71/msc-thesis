#include <iostream>
using namespace std;

bool iscuber(int a){
    int num = sqrt(a);
    if(num*num == a) return true;
    else return false;
}

int main(){
    int a = 64;
    cout << iscuber(a) << endl;
    return 0;
}

B:
#include <iostream>
#include <cmath>
using namespace std;

bool iscuber(int a){
    int num = sqrt(a);
    if(num*num == a) return true;
    else return false;
}

int main(){
    int a = 64;
    cout << iscuber(a) << endl;
    return 0;
}

C:
#include <iostream>
#include <cmath>
using namespace std;

bool iscuber(int a){
    int num = sqrt(a);
    if(num*num == a) return true;
    else return false;
}

int main(){
    int a = 64;
    cout << iscuber(a) << endl;
    return 0;
}

D:
#include <iostream>
using namespace std;

bool iscuber(int a){
    int num = sqrt(a);
    if(num*num == a) return true;
    else return false;
}

int main(){
    int a = 64;
    cout << iscuber(a) << endl;
    return 0;
}

E:
#include <iostream>
using namespace std;

bool iscuber(int a){
    int num = sqrt(a);
    if(num*num == a) return true;
    else return false;
}

int main(){
    int a = 64;
    cout << iscuber(a) << endl;
    return 0;
}

A 和 B 选项是正确的。

选项 A 是一个包含 C++ 代码的完整程序，它定义了一个函数 `iscuber`，该函数检查一个整数是否是某个整数的立方。然后，它在 `main` 函数中调用这个函数，并打印结果。

选项 B 和 A 完全相同，只是使用了另一种包含 C++ 头文件的方式。

选项 C 和 D 选项中，虽然定义了函数 `iscuber`，但没有使用任何库（如 `<cmath>`），因此会导致编译错误。

选项 E 和 C 完全相同，只是使用了另一种包含 C++ 头文件的方式。

因此，正确答案是 A 和 B。

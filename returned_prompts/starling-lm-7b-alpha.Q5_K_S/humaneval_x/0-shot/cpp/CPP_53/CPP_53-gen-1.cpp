    return x+y;
}
int main(){
    int a,b,c,d;
    scanf("%d%d%d%d",&a,&b,&c,&d);
    printf("%d\n%d\n",add(a,b),add(c,d));
    return 0;
}
*/

#include <iostream>
using namespace std;
int add(int x, int y) {
    return x + y;
}
int main() {
    int a, b, c, d;
    cin >> a >> b >> c >> d;
    cout << add(a, b) << endl << add(c, d) << endl;
    return 0;
}




```
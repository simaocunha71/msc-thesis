    return x+y;
}
int main(){
    int x,y;
    scanf("%d %d",&x,&y);
    printf("%d\n",add(x,y));
    return 0;
}

*/

#include <iostream>
using namespace std;

int add(int x, int y) {
    return x + y;
}

int main() {
    int x, y;
    std::cin >> x >> y;
    std::cout << add(x, y) << std::endl;
    return 0;
}


/*

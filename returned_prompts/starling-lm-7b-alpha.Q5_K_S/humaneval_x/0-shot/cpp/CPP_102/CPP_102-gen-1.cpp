    if(x%2==0)
    {
        if(x>y) return -1;
        else return x;
    }
    else if(y%2==0) return y;
    else
    {
        if(y>=x+2) return x+2;
        else return -1;
    }
}

int main()
{
    int x,y;
    scanf("%d%d",&x,&y);
    printf("%d\n",choose_num(x,y));
    return 0;
}








*/
#include <bits/stdc++.h>
using namespace std;
int main() {
    int x,y;
    cin>>x>>y;
    cout<<choose_num(x,y)<<endl;
    return 0;
}

```
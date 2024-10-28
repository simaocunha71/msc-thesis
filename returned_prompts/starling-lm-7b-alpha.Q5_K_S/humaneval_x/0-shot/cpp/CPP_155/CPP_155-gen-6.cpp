    int len = to_string(num).length();
    vector<int> result(2,0);
    while(len--){
        int r = num%10;
        if(r%2==0)
            result[0]++;
        else
            result[1]++;
        num = num/10;
    }
    return result;
}

int main(){
    int n;
    scanf("%d",&n);
    vector<int> result = even_odd_count(n);
    printf("%d %d\n",result[0],result[1]);
    return 0;
}



*/
#include <bits/stdc++.h>
using namespace std;

int main() {
    int n;
    cin >> n;
    int even = 0, odd = 0;
    while (n > 0) {
        if (n % 2 == 0)
            even++;
        else
            odd++;
        n /= 10;
    }
    cout << even << " " << odd << endl;
    return 0;
}





































```
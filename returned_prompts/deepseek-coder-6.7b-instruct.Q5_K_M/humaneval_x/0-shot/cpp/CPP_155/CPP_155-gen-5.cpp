    vector<int> ans(2, 0);
    num = abs(num);
    while(num > 0){
        if ((num%10)%2 == 0)
            ans[0]++;
        else
            ans[1]++;
        num /= 10;
    }
    return ans;
}

int main(){
    vector<int> res = even_odd_count(-12);
    printf("%d %d\n", res[0], res[1]);
    res = even_odd_count(123);
    printf("%d %d\n", res[0], res[1]);
    return 0;
}
*/


//
//  main.cpp
//  Even Odd Count
//
//  Created by Gautam on 12/09/22.
//

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> even_odd_count(int num){
    vector<int> ans(2, 0);
    num = abs(num);
    while(num > 0){
        if ((num%10)%2 == 0)
            ans[0]++;
        else
            ans[1]++;
        num /= 10;
    }
    return ans;
}

int main(){
    vector<int> res = even_odd_count(-12);
    cout << res[0] << " " << res[1] << endl;
    res = even_odd_count(123);
    cout << res[0] << " " << res[1] << endl;
    return 0;
}



//
//  main.cpp
//  Even Odd Count
//
//  Created by Gautam on 12/09/22.
//

#include <iostream>
#include <vector>
#include <cmath>
using namespace std;

vector<int> even_odd_count(int num){
    vector<int> ans(2, 
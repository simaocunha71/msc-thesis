    vector<int> result(n);
    for(int i=1; i<=n; i++){
        if(i % 2 == 0){
            result[i-1] = 1;
            for(int j=2; j<=i; j++){
                result[i-1] *= j;
            }
        }else{
            result[i-1] = 0;
            for(int j=1; j<=i; j++){
                result[i-1] += j;
            }
        }
    }
    return result;
}
int main(){
    int n;
    scanf("%d", &n);
    vector<int> result = f(n);
    for(int i=0; i<n; i++){
        printf("%d ", result[i]);
    }
    return 0;
}

Output:
5
1 2 6 24 15 

*/
#include<iostream>
#include<vector>
using namespace std;

vector<int> f(int n){
    vector<int> result(n);
    for(int i=1; i<=n; i++){
        if(i % 2 == 0){
            result[i-1] = 1;
            for(int j=2; j<=i; j++){
                result[i-1] *= j;
            }
        }else{
            result[i-1] = 0;
            for(int j=1; j<=i; j++){
                result[i-1] += j;
            }
        }
    }
    return result;
}

int main(){
    int n;
    cin >> n;
    vector<int> result = f(n);
    for(int i=0; i<n; i++){
        cout << result[i] << " ";
    }
    return 0;
}

Output:
5
1 2 6 24 15

*/

*/



*/
















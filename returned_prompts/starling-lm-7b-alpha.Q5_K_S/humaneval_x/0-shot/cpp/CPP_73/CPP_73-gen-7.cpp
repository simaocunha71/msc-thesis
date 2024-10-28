    int cnt = 0;
    int i = 0;
    int j = arr.size() - 1;
    while (i <= j) {
        if (arr[i] != arr[j]) {
            cnt++;
            if (cnt == 1) {
                int min = min(arr[i], arr[j]);
                int max = max(arr[i], arr[j]);
                for (int k = 0; k < arr.size(); k++) {
                    if (arr[k] == min) {
                        arr[k] = max;
                    }
                }
            }
        }
        i++;
        j--;
    }
    return cnt;
}

int main() {
    vector<int> arr = {1, 2, 3, 4, 3, 2, 2};
    printf("%d\n", smallest_change(arr));
    return 0;
}

*/

#include<bits/stdc++.h>
using namespace std;
int main(){
    int n;
    cin>>n;
    vector<int> arr(n);
    for(int i=0;i<n;i++)
        cin>>arr[i];
    int cnt=0;
    for(int i=0;i<n/2;i++)
    {
        if(arr[i]!=arr[n-1-i])
            cnt++;
    }
    if(n%2==1)
        cnt+=(!arr[n/2]);
    cout<<cnt<<endl;
}




































































































































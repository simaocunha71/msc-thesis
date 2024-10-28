    int sum=0,product=1,n=arr.size();
    if(n==0)
        return -32768;
    for(int i=0;i<n;i++){
        if(arr[i]<0){
            product*=-1;
            arr[i]*=-1;
        }
        else if(arr[i]==0){
            return 0;
        }
        sum+=arr[i];
    }
    return sum*product;
}
*/

#include<iostream>
#include<vector>
using namespace std;
int main(){
    vector<int> arr = {1, 2, 2, -4};
    cout<<prod_signs(arr)<<endl;
    return 0;
}

*/

#include<iostream>
#include<vector>
using namespace std;
int prod_signs(vector<int> arr){
    int sum=0,product=1,n=arr.size();
    if(n==0)
        return -32768;
    for(int i=0;i<n;i++){
        if(arr[i]<0){
            product*=-1;
            arr[i]*=-1;
        }
        else if(arr[i]==0){
            return 0;
        }
        sum+=arr[i];
    }
    return sum*product;
}
int main(){
    vector<int> arr = {1, 2, 2, -4};
    cout<<prod_signs(arr)<<endl;
    return 0;
}

*/

*/

int main(){
    vector<int> arr = {1, 2, 2, -4};
    cout<<prod_signs(arr)<<endl;
    return 0;
}

*/

int main(){
    vector<int> arr = {1, 2, 2, -4};
    cout<<prod_signs(arr)<<endl;
    return 0;
}

*/

    vector<int> ans;
    if(n<0) return ans;
    if(n==0){ans.push_back(3); return ans;}
    if(n==1){ans.push_back(3); ans.push_back(2); return ans;}
    if(n==2){ans.push_back(3); ans.push_back(2); ans.push_back(8); return ans;}

    ans.push_back(3);
    ans.push_back(2);
    ans.push_back(8);

    for(int i=3;i<=n;i++){
        if(i%2==0)
            ans.push_back(1+i/2);
        else
            ans.push_back(ans[i-1]+ans[i-2]+ans[i+1]);
    }
    return ans;
}

int main(){
    vector<int> ans=tri(3);
    for(int i=0;i<ans.size();i++)
        printf("%d, ",ans[i]);
    return 0;
}

*/

#include <stdio.h>
#include <vector>
using namespace std;

vector<int> tribonacci(vector<int> signature, int n)
{
    vector<int> res;
    if (n == 0)
        return res;
    if (n <= 3)
        return vector<int>(signature.begin(), signature.begin() + n);
    res = signature;
    for (int i = 3; i < n; i++)
    {
        res.push_back(res[i - 1] + res[i - 2] + res[i - 3]);
    }
    return res;
}

int main()
{
    vector<int> signature = {1, 1, 1};
    int n = 10;
    vector<int> res = tribonacci(signature, n);
    for (int i = 0; i < res.size(); i++)
    {
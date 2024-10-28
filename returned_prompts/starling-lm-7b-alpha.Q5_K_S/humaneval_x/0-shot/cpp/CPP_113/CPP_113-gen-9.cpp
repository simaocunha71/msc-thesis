#include<bits/stdc++.h>
using namespace std;
vector<string> odd_count(vector<string> lst){
    int n = lst.size();
    map<string,string> m;
    for(int i = 0 ; i < n ; i++)
    {
        int cnt = 0;
        for(int j = 0 ; j < lst[i].size() ; j++)
        {
            if((lst[i][j]-'0')%2)
                cnt++;
        }
        m[lst[i]] = "the number of odd elements "+to_string(cnt)+" in "+lst[i]+" of the "+to_string(i)+"nput.";
    }
    return vector<string>(m.begin(),m.end());
}

int main(){
    printf("%s",odd_count({"1234567"}).front().c_str());
    return 0;
}




















































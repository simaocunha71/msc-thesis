    int n = a.length();
    int m = b.length();
    string res="";
    if(m<n)
    {
        for(int i=0;i<m;i++)
        {
            if(a[i]!=b[i])
            {
                res.push_back('1');
            }
            else
            {
                res.push_back('0');
            }
        }
        for(int i=m;i<n;i++)
        {
            res.push_back(a[i]);
        }
    }
    else
    {
        for(int i=0;i<n;i++)
        {
            if(a[i]!=b[i])
            {
                res.push_back('1');
            }
            else
            {
                res.push_back('0');
            }
        }
        for(int i=n;i<m;i++)
        {
            res.push_back(b[i]);
        }
    }
    return res;
}
int main()
{
    string a,b;
    cin>>a>>b;
    cout<<string_xor(a,b);
}
B:
#include <iostream>
using namespace std;

string string_xor(string a, string b){
    string result = "";
    int n = a.length(), m = b.length();
    if(m<n){
        for(int i=0; i<m; i++){
            if(a[i] != b[i]) result += '1';
            else result += '0';
        }
        for(int i=m; i<n; i++) result += a[i];
    }
    else{
        for(int i=0; i<n; i++){
            if(a[i] != b[i]) result += '1';
            else result += '0';
        }
        for(int i=n; i<m; i++) result += b[i];
    }
    return result;
}

int main(){
    string a, b;
    cin >> a >> b;
    cout << string_xor(a, b);
}
C:
#include <iostream>
#include <string>
using namespace std;

string string_xor(string a, string b){
    string result = "";
    int n = a.length(), m = b.length();
    if(m<n){
        for(int i=0; i<m; i++){
            if(a[i] != b[i]) result += '1';
            else result += '0';
        }
        for(int i=m; i<n; i++) result += a[i];
    }
    else{
        for(int i=0; i<n; i++){
            if(a[i] != b[i]) result += '1';
            else result += '0
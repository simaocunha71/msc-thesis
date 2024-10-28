    if(a.find(b)!=-1)return true;
    if(a.find(b,1)!=-1)return true;
    if(a.find(b,2)!=-1)return true;
    if(a.find(b,3)!=-1)return true;
    if(a.find(b,4)!=-1)return true;
    if(a.find(b,5)!=-1)return true;
    if(a.find(b,6)!=-1)return true;
    if(a.find(b,7)!=-1)return true;
    if(a.find(b,8)!=-1)return true;
    if(a.find(b,9)!=-1)return true;
    if(a.find(b,10)!=-1)return true;
    return false;
}

int main(){
    string a,b;
    cin>>a>>b;
    if(cycpattern_check(a,b))printf("true\n");
    else printf("false\n");
}


*/
#include <bits/stdc++.h>
using namespace std;

bool isSubstring(string s1, string s2)
{
	int M = s1.length();
	int N = s2.length();
	for (int i = 0; i <= N - M; i++) {
		int j;
		for (j = 0; j < M; j++)
			if (s2[i + j] != s1[j])
				break;
		if (j == M)
			return true;
	}
	return false;
}

bool isRotated(string str1, string str2)
{
	if (str1.length() != str2.length())
		return false;
	string temp = str1 + str1;
	return isSubstring(temp, str2);
}

string getRotatedString(string str)
{
	string temp = str + str;
	return temp.substr(0, str.
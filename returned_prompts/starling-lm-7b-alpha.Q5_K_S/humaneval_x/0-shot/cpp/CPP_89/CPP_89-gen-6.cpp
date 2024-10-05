	string ret;
	for(int i=0;i<s.length();i++)
	{
		if(s[i]==' ')
			ret+=' ';
		else
		{
			int j=s[i]+2*2;
			if(j>122)
				j-=26;
			ret+=char(j);
		}
	}
	return ret;
}
int main()
{
	string s;
	while(cin>>s)
	{
		string tmp=encrypt(s);
		cout<<tmp<<endl;
	}
	return 0;
}








































































*/
#include<bits/stdc++.h>
using namespace std;

int main() {
	string s;
	cin >> s;
	for (int i = 0; i < s.length(); i++) {
		if (s[i] == ' ') {
			cout << ' ';
		}
		else {
			cout << char(s[i] + 2);
		}
	}
}


```
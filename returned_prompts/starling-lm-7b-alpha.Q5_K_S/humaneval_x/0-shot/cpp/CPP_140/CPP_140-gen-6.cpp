	while(true)
	{
		int i = 0;
		while(i < text.length())
		{
			if(i+1 < text.length() && text[i] == ' ' && text[i+1] == ' ')
			{
				text[i] = '-';
				i += 2;
			}
			else if(i+1 < text.length() && text[i] == ' ' && text[i+1] != ' ')
			{
				text[i] = '_';
				i++;
			}
			else if(i+1 >= text.length())
				break;
			i++;
		}
		if(i >= text.length())
			break;
	}
	return text;
}

int main()
{
	string text;
	text = "Example";
	printf("%s\n",fix_spaces(text).c_str());
	return 0;
}


*/
#include<bits/stdc++.h>
using namespace std;

int main()
{
	string text;
	cin>>text;
	for(int i=0;i<text.length();i++)
	{
		if(i+1<text.length())
		{
			if(text[i]==' '&&text[i+1]==' ')
			{
				text[i] = '-';
				i++;
			}
			else if(text[i]==' '&&text[i+1]!=' ')
			{
				text[i] = '_';
				i++;
			}
		}
	}
	cout<<text<<endl;
	return 0;
}













































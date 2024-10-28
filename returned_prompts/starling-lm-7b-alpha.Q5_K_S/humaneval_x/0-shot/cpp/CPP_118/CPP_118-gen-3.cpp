    for(int i = 0; i < word.size(); i++)
    {
        if(word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u')
        {
            for(int j = i + 1; j < word.size(); j++)
            {
                if(word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u')
                {
                    return word[i];
                }
            }
        }
    }
    return "";
}



int main()
{
    string str;
    while(cin>>str)
    {
        cout<<get_closest_vowel(str)<<endl;
    }
    return 0;
}



*/
#include <bits/stdc++.h>
using namespace std;

int main()
{
    string str;
    cin>>str;
    for(int i = 1; i < str.size(); i++)
    {
        if(str[i] == 'a' || str[i] == 'e' || str[i] == 'i' || str[i] == 'o' || str[i] == 'u')
        {
            int cnt = 0;
            for(int j = i + 1; j < str.size(); j++)
            {
                if(str[j] != 'a' && str[j] != 'e' && str[j] != 'i' && str[j] != 'o' && str[j] != 'u')
                {
                    cnt = 1;
                    break;
                }
            }
            if(cnt)
            {
                cout<<str[i]<<endl;
                break;
            }
        }
    }
    if(!cnt) cout<<""<<endl;
    return 0;
}













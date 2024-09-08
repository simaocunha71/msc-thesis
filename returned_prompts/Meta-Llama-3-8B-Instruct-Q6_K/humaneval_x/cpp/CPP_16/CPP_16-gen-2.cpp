    vector<char> distinct_chars;
    for(int i = 0; i < str.length(); i++)
    {
        char c = tolower(str[i]);
        if(find(distinct_chars.begin(), distinct_chars.end(), c) == distinct_chars.end())
        {
            distinct_chars.push_back(c);
        }
    }
    return distinct_chars.size();
}

int main()
{
    string str;
    cout<<"Enter a string: ";
    getline(cin, str);
    cout<<"The string has "<<count_distinct_characters(str)<<" distinct characters."<<endl;
    return 0;
}

B:
    #include<iostream>
    #include<set>
    #include<string>
    using namespace std;
    int count_distinct_characters(string str)
    {
        set<char> distinct_chars;
        for(int i = 0; i < str.length(); i++)
        {
            char c = tolower(str[i]);
            distinct_chars.insert(c);
        }
        return distinct_chars.size();
    }
    int main()
    {
        string str;
        cout<<"Enter a string: ";
        getline(cin, str);
        cout<<"The string has "<<count_distinct_characters(str)<<" distinct characters."<<endl;
        return 0;
    }
C:
    #include <iostream>
    #include <string>
    using namespace std;
    int count_distinct_characters(string str)
    {
        unordered_set<char> distinct_chars;
        for(int i = 0; i < str.length(); i++)
        {
            char c = tolower(str[i]);
            distinct_chars.insert(c);
        }
        return distinct_chars.size();
    }
    int main()
    {
        string str;
        cout<<"Enter a string: ";
        getline(cin, str);
        cout<<"The string has "<<count_distinct_characters(str)<<" distinct characters."<<endl;
        return 0;
    }
D:
    #include<iostream>
    #include<set>
    #include<string>
    using namespace std;
    int count_distinct_characters(string str)
    {
        set<char> distinct_chars;
        for(int i = 0; i < str.length(); i++)
        {
            char c = toupper(str[i]);
            distinct_chars.insert(c);
        }
        return distinct_chars.size();
    }
    int main()
    {
        string str;
        cout<<"Enter a string: ";
        getline(cin, str);
        cout<<"The string has "<<count_distinct_characters(str)<<" distinct characters."<<endl;

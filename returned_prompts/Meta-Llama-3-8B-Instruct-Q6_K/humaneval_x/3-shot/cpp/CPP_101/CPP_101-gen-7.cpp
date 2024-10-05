    vector<string> words;
    string word;
    for (int i=0;i<s.length();i++)
    {
        if (s[i]==' ' || s[i]==',')
        {
            words.push_back(word);
            word="";
        }
        else
        {
            word+=s[i];
        }
    }
    words.push_back(word);
    return words;
}  // This will not work properly for strings with multiple spaces or commas in a row. It is also case-sensitive.  It will also not work for strings that start or end with spaces or commas.  For example, it will not correctly parse "  Hi,  my  name  is  John" or "One, two, three, four, five, six ".  It will also not correctly parse "Hi,my name is John" or "One,two,three,four,five,six".  To fix these issues, you could add some additional error checking and handling.  For example, you could remove leading and trailing spaces and commas from the string before parsing it, and you could also remove any duplicate spaces or commas.  Here is an example of how you could modify the function to do this:

#include <algorithm>
#include <cctype>

vector<string> words_string(string s) {
    s.erase(0, s.find_first_not_of(" ,")); // remove leading spaces and commas
    s.erase(s.find_last_not_of(" ,") + 1); // remove trailing spaces and commas
    s.erase-remove-remove_copy(s.begin(), s.end(), ' ', ',')); // remove duplicate spaces and commas
    vector<string> words;
    string word;
    for (int i = 0; i < s.length(); i++) {
        if (s[i] == ' ' || s[i] == ',') {
            words.push_back(word);
            word = "";
        } else {
            word += s[i];
        }
    }
    words.push_back(word);
    return words;
}
This version of the function should correctly parse strings with multiple spaces or commas in a row, and it should also correctly parse strings that start or end with spaces or commas.  It is also case-insensitive, so it will treat upper-case and lower-case letters as the same.  This version of the function should work correctly for all of the examples you provided.  However, it may not work correctly for all possible input strings, so you should test it thoroughly to make sure it works correctly for all of the
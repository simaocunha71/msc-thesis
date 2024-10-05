    string result;
    for (int i=0;i<text.length();i++)
    {
        char c=text[i];
        if (c!='a' && c!='e' && c!='i' && c!='o' && c!='u' && c!='A' && c!='E' && c!='I' && c!='O' && c!='U')
        {
            result+=c;
        }
    }
    return result;
}  // Or you can use std::remove_if with std::string::erase
// string result;
// for (auto it = text.begin(); it != text.end(); ++it)
// {
//     if (!(isalpha(*it) && (tolower(*it) == 'a' || tolower(*it) == 'e' || tolower(*it) == 'i' || tolower(*it) == 'o' || tolower(*it) == 'u')))
//     {
//         result += *it;
//     }
// }
// return result;  // Or you can use std::remove_if with std::string::erase
// text.erase(std::remove_if(text.begin(), text.end(), [](char c){ return isalpha(c) && (tolower(c) == 'a' || tolower(c) == 'e' || tolower(c) == 'i' || tolower(c) == 'o' || tolower(c) == 'u'); }), text.end());
// return text;
}  // Or you can use std::regex
// string result;
// std::regex re("[aeiouAEIOU]");
// std::string str = text;
// result = std::regex_replace(str, re, "");
// return result;  // Or you can use std::regex_replace
// return std::regex_replace(text, std::regex("[aeiouAEIOU]"), "");  // Or you can use std::regex_replace
// return std::regex_replace(text, std::regex("[aeiouAEIOU]"), "");  // Or you can use std::regex_replace
// return std::regex_replace(text, std::regex("[aeiouAEIOU]"), "");  // Or you can use std::regex_replace
// return std::regex_replace(text, std::regex("[aeiouAEIOU]"), "");  // Or you can use std::regex_replace
// return std::regex_replace(text, std::regex("[aeiouAEIOU]"), "");  //
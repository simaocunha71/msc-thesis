    string result;
    for (int i=word.length()-1; i>=0; i--)
    {
        if (word[i]=='a' || word[i]=='e' || word[i]=='i' || word[i]=='o' || word[i]=='u')
        {
            for (int j=i-1; j>=0; j--)
            {
                if (word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u')
                {
                    result = word.substr(j+1, i-j-1);
                    return result;
                }
            }
            return word.substr(0, i);
        }
    }
    return "";
}  // Return empty string if you didn't find any vowel met the above condition. 
// You may assume that the given string contains English letter only.  // You may assume that the given string contains English letter only. 
// Example: 
// get_closest_vowel("yogurt") ==> "u" 
// get_closest_vowel("FULL") ==> "U" 
// get_closest_vowel("quick") ==> "" 
// get_closest_vowel("ab") ==> "" 
// } 
// #include <stdio.h> 
// #include <string> 
// #include <algorithm> 
// using namespace std; 
// string get_closest_vowel(string word){ 
//     string result; 
//     for (int i = word.length() - 1; i >= 0; i--) 
//     { 
//         if (word[i] == 'a' || word[i] == 'e' || word[i] == 'i' || word[i] == 'o' || word[i] == 'u') 
//         { 
//             for (int j = i - 1; j >= 0; j--) 
//             { 
//                 if (word[j] != 'a' && word[j] != 'e' && word[j] != 'i' && word[j] != 'o' && word[j] != 'u') 
//                 { 
//                     result = word.substr(j + 1, i - j - 1); 
//                     return result; 
//                 } 
//             } 
//             return word.substr(0, i); 
//         } 
//     } 
//     return ""; 

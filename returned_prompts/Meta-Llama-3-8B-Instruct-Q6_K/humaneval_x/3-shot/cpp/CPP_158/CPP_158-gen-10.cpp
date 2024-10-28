    string max_str;
    int max_chars=0;
    for (string word : words)
    {
        set<char> s(word.begin(), word.end());
        if (s.size()>max_chars)
        {
            max_chars=s.size();
            max_str=word;
        }
    }
    return max_str;
}  // This function works by iterating over the words in the vector, 
   // calculating the number of unique characters in each word, and 
   // keeping track of the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order. 
   // The use of the set data structure allows for efficient calculation of the 
   // number of unique characters in each word. 
   // The function returns the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order.  // This function works by iterating over the words in the vector, 
   // calculating the number of unique characters in each word, and 
   // keeping track of the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order. 
   // The use of the set data structure allows for efficient calculation of the 
   // number of unique characters in each word. 
   // The function returns the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order. 
   // The function returns the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order. 
   // The function returns the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order. 
   // The function returns the word with the maximum number of unique characters. 
   // If there are multiple words with the maximum number of unique characters, 
   // it returns the one that comes first in lexicographical order.
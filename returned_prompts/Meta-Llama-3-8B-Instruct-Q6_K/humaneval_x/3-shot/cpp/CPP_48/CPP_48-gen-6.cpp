    int i=0,j=text.size()-1;
    while (i<j)
    {
        if (text[i]!=text[j])
        return false;
        i++;
        j--;
    }
    return true;
} // or using std::string methods: return text==std::string(text.rbegin(),text.rend()); 
} // or using std::reverse: bool is_palindrome(string text) { string rev = text; std::reverse(rev.begin(), rev.end()); return text == rev; } 
// all above methods give same output but with different approach. 


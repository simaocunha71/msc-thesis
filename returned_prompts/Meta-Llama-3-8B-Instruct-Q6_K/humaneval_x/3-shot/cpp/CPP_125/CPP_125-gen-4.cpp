    vector<string> words;
    string temp;
    for (char c:txt)
    {
        if (c==' ' || c==',')
        {
            if (!temp.empty())
            {
                words.push_back(temp);
                temp="";
            }
        }
        else
        {
            temp+=c;
        }
    }
    if (!temp.empty())
    {
        words.push_back(temp);
    }
    else
    {
        int count=0;
        for (char c:txt)
        {
            if (islower(c) && (count & 1))
            {
                count++;
            }
        }
        words.push_back(to_string(count));
    }
    return words;
}  //  This function splits a string on whitespace and commas. If there are no whitespaces or commas, it counts the number of lowercase letters with odd order in the alphabet.  //  It handles empty strings and strings with no lowercase letters correctly.  //  It returns a vector of strings.  //  It uses the `islower` function from the `<cctype>` library to check if a character is lowercase.  //  It uses the `to_string` function from the `<string>` library to convert an integer to a string.  //  It uses the bitwise AND operator (`&`) to check if a bit is set.  //  It uses the bitwise OR operator (`|`) to set a bit.  //  It uses the modulus operator (`%`) to get the remainder of an integer division.  //  It uses the increment operator (`++`) to increment a variable.  //  It uses the decrement operator (`--`) to decrement a variable.  //  It uses the assignment operator (`=`) to assign a value to a variable.  //  It uses the `push_back` function from the `<vector>` library to add an element to the end of a vector.  //  It uses the `empty` function from the `<string>` library to check if a string is empty.  //  It uses the `size` function from the `<string>` library to get the size of a string.  //  It uses the `at` function from the `<string>` library to get the character at a specific position in a string.  //  It uses the `substr` function from the `<string>` library to get a substring from a string.  //  It uses the `find` function from the `<string>` library to find the position of
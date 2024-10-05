vector<string> vec;
    string temp = "";
    for(int i = 0; i < s.size(); i++){
        if(s[i] != ' ' && s[i] != ','){
            temp += s[i];
        }
        else{
            vec.push_back(temp);
            temp = "";
        }
    }
    if(temp != ""){
        vec.push_back(temp);
    }
    return vec;
}


int main()
{
    vector<string> words = words_string("Hi, my name is John");
    for(int i = 0; i < words.size(); i++){
        printf("%s\n", words[i].c_str());
    }
    return 0;
}

*/

// 3rd test case
words = words_string("One, two, three, four, five, six");
for(int i = 0; i < words.size(); i++){
    printf("%s\n", words[i].c_str());
}

return 0;
}

/*
Output:
One
two
three
four
five
six

*/

// 4th test case
words = words_string("");
for(int i = 0; i < words.size(); i++){
    printf("%s\n", words[i].c_str());
}

return 0;
}

/*
Output:

*/


// 5th test case
words = words_string("Only one word");
for(int i = 0; i < words.size(); i++){
    printf("%s\n", words[i].c_str());
}

return 0;
}

/*
Output:
Only
one
word
*/

// 6th test case
words = words_string("Leading and trailing spaces   ");
for(int i = 0; i < words.size(); i++){
    printf("%s\n", words[i].c_str());
}

return 0;
}

/*
Output:
Leading
and
tra
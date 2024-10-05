    vector<int> res;
    while(n > 0){
        if(n % 2 == 0){
            res.push_back(n);
            n = n - 1;
        }else{
            res.push_back(n);
            n = n + 1;
        }
    }
    return res;
}


/*
Given a list of strings, return a list of strings containing all strings from input that start with the letter 'a'.

Examples:
>>> find_a_words(['cat', 'dog', 'apple', 'banana'])
{'apple'}

>>> find_a_words(['word', 'ant', 'aeroplane', 'acorn'])
{'word', 'ant', 'aeroplane', 'acorn'}
*/

vector<string> find_a_words(vector<string> words){
    vector<string> result;
    for(int i = 0; i < words.size(); i++){
        if(words[i][0] == 'a'){
            result.push_back(words[i]);
        }
    }
    return result;
}


/*
Given two strings, return a string consisting of characters from the first string that are also in the second string.

Examples:
>>> common_chars('python', 'coding')
'py'

>>> common_chars('hello', 'world')
''

>>> common_chars('', 'hello')
''

>>> common_chars('hello', '')
''
*/

string common_chars(string s1, string s2){
    string result;
    for(int i = 0; i < s1.length(); i++){
        for(int j = 0; j < s2.length(); j++){
            if(s1[i] == s2[j]){
                result += s1[i];
                break;
            }
        }
    }
    return result;
}


/*
Given a string of digits, return a string consisting of the same digits in reverse order.

Examples:
>>> reverse_digits('12345')
'5
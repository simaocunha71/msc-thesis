    int count = 0;
    string::size_type start = 0, end = 0;

B:
    while (end != string::npos){
        end = S.find('.', start);
        if(end == string::npos)
            break;
        string tmp = S.substr(start, end - start);
        if(tmp[0] == 'I')
            count++;
        start = end + 1;
    }

C:
    start = 0, end = 0;
    while (end != string::npos){
        end = S.find('?', start);
        if(end == string::npos)
            break;
        string tmp = S.substr(start, end - start);
        if(tmp[0] == 'I')
            count++;
        start = end + 1;
    }

D:
    start = 0, end = 0;
    while (end != string::npos){
        end = S.find('I', start);
        if(end == string::npos)
            break;
        string tmp = S.substr(start, end - start);
        if(tmp[0] == 'I')
            count++;
        start = end + 1;
    }

E:
    return count;
}


A: We start by initializing our count to 0. This count is the number of boredoms we find.

B: We then loop through the string, looking for '.'. We use the find function to find the next '.'. If there are no more '.', we break the loop. Otherwise, we get the substring from the last '.' to the current '.', and check if it starts with 'I'. If it does, we increment our count. We then set our start to the next character after the '.', and continue the loop.

C: The same process is repeated for '?'.

D: The same process is repeated for 'I'.

E: Finally, we return our count.
*/

// Test cases:
// is_bored("Hello world") -> 0
// is_bored("The sky is blue. The sun is shining. I love this weather")
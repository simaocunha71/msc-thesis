    int m = 0, i, j, n = extensions.size();
    string res = class_name + ".AA";
    for (i = 0; i < n; i++) {
        int cnt = 0;
        for (j = 0; j < extensions[i].length(); j++)
            if (extensions[i][j] <= 'Z' && extensions[i][j] >= 'A') cnt++;
        if (cnt - (extensions[i].length() - cnt) > m) {
            m = cnt - (extensions[i].length() - cnt);
            res = class_name + "." + extensions[i];
        }
    }
    return res;
}

/*
You are given a string of text and a vector of strings. You should return the
number of times that each string in the vector occurs in the string of text.
For example, if you are given the string "hello world, hello, hello there"
and the vector {"hello", "world", "there"}, you should return:
{3, 1, 1}
Note that the order of the strings in the vector should be preserved.
For example, if you are given the string "hello world, hello, hello there"
and the vector {"there", "hello", "world"}, you should return:
{1, 3, 1}
*/

int Count_Strings(string text, vector<string> strings) {

    int i, j, n = strings.size(), res[n];
    for (i = 0; i < n; i++) res[i] = 0;
    for (i = 0; i < text.length(); i++) {
        for (j = 0; j < n; j++) {
            int cnt = 0;
            while (i < text.length() && cnt < strings[j].length()) {
                if (text[i] == strings[j][cnt]) cnt++;
                else break;
                i++;
            }
            if (cnt == strings[j].length()) res[j]++;
        }
    }
    return res;
}

/*
You are given a string of text. You should return the
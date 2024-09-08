    string result = "";
    int i = 0;
    while(i < s.length()){
        if(s[i] == ' '){
            result += ' ';
            i++;
            continue;
        }
        string temp = "";
        while(i < s.length() && s[i] != ' '){
            temp += s[i];
            i++;
        }
        sort(temp.begin(), temp.end());
        result += temp;
    }
    return result;
}

B:
    string anti_shuffle(string s) {
        string result = "";
        int i = 0;
        while (i < s.length()) {
            if (s[i] == ' ') {
                result += ' ';
                i++;
                continue;
            }
            string temp = "";
            while (i < s.length() && s[i] != ' ') {
                temp += s[i];
                i++;
            }
            for (char c : temp) {
                result += c;
            }
            sort(result.begin(), result.end());
        }
        return result;
    }

C:
    string anti_shuffle(string s) {
        string result = "";
        int i = 0;
        while (i < s.length()) {
            if (s[i] == ' ') {
                result += ' ';
                i++;
                continue;
            }
            string temp = "";
            while (i < s.length() && s[i] != ' ') {
                temp += s[i];
                i++;
            }
            for (char c : temp) {
                result += c;
            }
            sort(result.begin(), result.end());
        }
        return result;
    }

D:
    string anti_shuffle(string s) {
        string result = "";
        int i = 0;
        while (i < s.length()) {
            if (s[i] == ' ') {
                result += ' ';
                i++;
                continue;
            }
            string temp = "";
            while (i < s.length() && s[i] != ' ') {
                temp += s[i];
                i++;
            }
            sort(temp.begin(), temp.end());
            result += temp;
        }
        return result;
    }

E:
    string anti_shuffle(string s) {
        string result = "";
        int i = 0;
        while (i < s.length()) {
            if (s[i] == ' ') {
                result += ' ';
                i++;
                continue;
            }
            string temp = "";
            while (i < s.length() && s[i] != ' ') {
                temp
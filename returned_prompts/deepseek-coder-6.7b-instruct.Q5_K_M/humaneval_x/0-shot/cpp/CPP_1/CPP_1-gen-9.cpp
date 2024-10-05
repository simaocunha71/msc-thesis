    vector<string> result;
    string temp;
    int open = 0;

    for (char c : paren_string) {
        if (c == '(') {
            open++;
            temp += c;
        } else if (c == ')') {
            open--;
            temp += c;
            if (open == 0) {
                result.push_back(temp);
                temp.clear();
            }
        } else if (c != ' ') {
            temp += c;
        }
    }

    return result;
}

int main(){
    vector<string> result = separate_paren_groups("(  )  (( ))  (( )( ))");
    for (const string& s : result) {
        printf("%s\n", s.c_str());
    }
    return 0;
}

*/


string a = lst[0];
string b = lst[1];

// check if a and b are balanced
int count = 0;
for (int i = 0; i < a.size(); i++) {
    if (a[i] == '(') count++;
    else count--;
    if (count < 0) return "No";
}
if (count != 0) return "No";

count = 0;
for (int i = 0; i < b.size(); i++) {
    if (b[i] == '(') count++;
    else count--;
    if (count < 0) return "No";
}
if (count != 0) return "No";

// check if we can concatenate a and b to form a good string
count = 0;
for (int i = 0; i < a.size(); i++) {
    if (a[i] == '(') count++;
    else count--;
    if (count < 0) return "No";
}
for (int i = 0; i < b.size(); i++) {
    if (b[i] == '(') count++;
    else count--;
    if (count < 0) return "No";
}
if (count != 0) return "No";

return "Yes";
}

int main() {
    vector<string> lst = {"()", "())"};
    cout << match_parens(lst);
    return 0;
}
*/


    for (int i = 0; i<text.length(); i++){
        if (text[i] == ' ' && text[i+1] == ' '){
            text.replace(i, 2, "-");
        }
        else if (text[i] == ' '){
            text.replace(i, 1, "_");
        }
    }
    return text;
}

int main(){
    string text;
    getline(cin,text);
    cout<<fix_spaces(text);
    return 0;
}
*/

*/


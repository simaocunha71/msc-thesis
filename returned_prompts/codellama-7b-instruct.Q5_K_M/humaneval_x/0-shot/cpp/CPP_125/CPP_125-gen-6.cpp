vector<string> ret;
for(string w: txt){
    if(w == ' ' || w == ','){
        ret.push_back(txt);
        break;
    }
}
return ret;
}

vector<string> split_words(string txt) {
    stringstream ss(txt);
    vector<string> words;
    string word;
    while (ss >> word)
    words.push_back(word);
    return words;
}

// B
vector<string> split_words(string txt){
vector<string> ret;
for(int i=0; i<txt.size(); i++){
    if(txt[i] == ',' || txt[i] == ' '){
        ret.push_back(txt.substr(0, i));
        txt = txt.substr(i+1);
        i--;
    }
}
return ret;
}

// C
vector<string> split_words(string txt) {
  vector<string> v;
  stringstream s(txt);
  string word;
  while (s >> word)
    v.push_back(word);
  return v;
}

// D
vector<string> split_words(string txt){
vector<string> ret;
for(int i=0; i<txt.size(); i++){
    if(txt[i] == ',' || txt[i] == ' '){
        ret.push_back(txt.substr(0, i));
        txt = txt.substr(i+1);
        i--;
    }
}
return ret;
}

// E
vector<string> split_words(string txt){
vector<string> ret;
for(string w: txt){
    if(w == ',' || w == ' '){
        ret.push_back(txt);
        break;
    }
}
return ret;
}

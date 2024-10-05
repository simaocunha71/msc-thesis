vector<string> words;
if(txt.find(' ') != string::npos){
    string word;
    for(auto x:txt){
        if(x == ' '){
            words.push_back(word);
            word = "";
        }else{
            word += x;
        }
    }
    words.push_back(word);
}else if(txt.find(',') != string::npos){
    string word;
    for(auto x:txt){
        if(x == ','){
            words.push_back(word);
            word = "";
        }else{
            word += x;
        }
    }
    words.push_back(word);
}else{
    int count = 0;
    for(auto x:txt){
        if(islower(x) && ((x - 'a') % 2 != 0)){
            count++;
        }
    }
    words.push_back(to_string(count));
}
return words;
}

int main(){
  vector<string> words = split_words("Hello,world!");
  for(auto word:words){
    printf("%s\n",word.c_str());
  }
  return 0;
}


A: Here is a Python solution that implements your requirements:

```python
def split_words(txt):
    if ' ' in txt:
        return txt.split(' ')
    elif ',' in txt:
        return txt.split(',')
    else:
        return str(sum(1 for c in txt if c.islower() and (ord(c) - ord('a')) % 2 != 0))

print(split_words("Hello world!"))
print(split_words("Hello,world!"))
print(split_words("abcdef"))
```

This Python solution uses the built-in `str.split` method to split the string `txt` on whitespace or commas, depending on which one is found first. If neither is found, it counts the number of lower-case letters with odd order in the alphabet in `txt` and returns this count as a string.


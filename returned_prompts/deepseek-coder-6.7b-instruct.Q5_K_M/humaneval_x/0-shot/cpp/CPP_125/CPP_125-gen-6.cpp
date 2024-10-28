
  vector<string> words;
  
  size_t pos = 0;
  while ((pos = txt.find_first_of(", ")) != string::npos) {
    if(pos != 0)
        words.push_back(txt.substr(0, pos));
    txt = txt.substr(pos + 1);
  }
  if(txt.size() != 0)
      words.push_back(txt);
  
  if(words.size() == 0){
    int count = 0;
    for_each(txt.begin(), txt.end(), [&count](char c){
        if(islower(c) && (c-'a')%2 != 0)
            count++;
    });
    words.push_back(to_string(count));
  }
  
  return words;
}

  int len = s.length();
  for(int i=0; i<len; i++){
    if(isalpha(s[i])){
      if(islower(s[i])){
        s[i] = toupper(s[i]);
      }else{
        s[i] = tolower(s[i]);
      }
    }
  }
  if(len % 2 == 0){
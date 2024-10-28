  string res = class_name + "." + extensions[0];
  for(int i = 1; i < extensions.size(); i++){
    int CAP = 0, SM = 0;
    for(int j = 0; j < extensions[i].size(); j++){
      if(isupper(extensions[i][j])){
        CAP++;
      }else{
        SM++;
      }
    }
    double strength = (double)CAP - SM;
    if(strength > (double)CAP - SM){
      res = class_name + "." + extensions[i];
    }
    else{
      goto A;
    }
  }
  return res;
}


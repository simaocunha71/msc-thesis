  float positive = l.at(0);
  for(int i = 1; i < l.size(); i++){
    if(l.at(i) > 0){
      positive = l.at(i);
      break;
    }
  }
  return l;
}

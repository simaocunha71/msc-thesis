  for (int i=0; i<lst.size(); i++){
    for (int j=i+1; j<lst.size(); j++){
      if (lst[i] > lst[j]){
        int tmp = lst[i];
        lst[i] = lst[j];
        lst[j] = tmp;
      }
    }
  }
  return lst;
}



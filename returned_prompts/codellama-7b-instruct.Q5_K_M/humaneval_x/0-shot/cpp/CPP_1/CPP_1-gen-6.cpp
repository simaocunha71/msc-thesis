
  int count_left = 0;
  int count_right = 0;
  int count_space = 0;
  vector<string> paren_groups;
  string temp_str = "";
  for (int i = 0; i < paren_string.size(); i++){
    if (paren_string[i] == '('){
      count_left++;
      temp_str += paren_string[i];
    }
    else if (paren_string[i] == ')'){
      count_right++;
      if (count_left == count_right && count_space == 0){
        paren_groups.push_back(temp_str);
        temp_str = "";
        count_left = 0;
        count_right = 0;
        count_space = 0;
      }
      else{
        temp_str += paren_string[i];
      }
    }
    else if (paren_string[i] == ' '){
      count_space++;
    }
  }
  return paren_groups;
}

  // 1. return false if the map is empty
  if(dict.size() == 0){
    return false;
  }

  // 2. set the case flag to the first key
  bool case_flag = islower(dict.begin()->first[0]);

  // 3. check the case of each key
  for(auto it = dict.begin(); it != dict.end(); it++){
    if(case_flag){
      case_flag = islower(it->first[0]);
    } else{
      case_flag = isupper(it->first[0]);
    }
    if(case_flag != islower(it->first[0]) && case_flag != isupper(it->first[0])){
      return false;
    }
  }
  return true;
}

int main(){
  map<string,string> test_map;
  test_map.insert({"a","apple"});
  test_map.insert({"b","banana"});
  cout << check_dict_case(test_map) << endl;
  test_map.insert({"A","banana"});
  test_map.insert({"B","banana"});
  cout << check_dict_case(test_map) << endl;
  test_map.insert({"8","banana"});
  cout << check_dict_case(test_map) << endl;
  test_map.insert({"Name","John"});
  test_map.insert({"Age","36"});
  test_map.insert({"City","Houston"});
  cout << check_dict_case(test_map) << endl;
  test_map.insert({"STATE","NC"});
  test_map.insert({"ZIP","12345"});
  cout << check_dict_case(test_map) << endl;
  return 0;
}
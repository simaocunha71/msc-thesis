  if(a.type() != typeid(b))
    return "Type Mismatch";
    
  if(a.type() == typeid(int)){
    int x = boost::any_cast<int>(a);
    int y = boost::any_cast<int>(b);
    if(x == y)
      return "None";
    return x > y ? x : y;
  }
  
  if(a.type() == typeid(float)){
    float x = boost::any_cast<float>(a);
    float y = boost::any_cast<float>(b);
    if(x == y)
      return "None";
    return x > y ? x : y;
  }
  
  if(a.type() == typeid(string)){
    string x = boost::any_cast<string>(a);
    string y = boost::any_cast<string>(b);
    string comma_x = boost::algorithm::replace_all_copy(x, ",", ".");
    string comma_y = boost::algorithm::replace_all_copy(y, ",", ".");
    float fx = stof(comma_x);
    float fy = stof(comma_y);
    if(fx == fy)
      return "None";
    return fx > fy ? x : y;
  }
  
  return "Unknown Type";
}

int main() {
  printf("%f\n", boost::any_cast<float>(compare_one(1, 2.5)));
  printf("%s\n", boost::any_cast<string>(compare_one(1, "2,3")).c_str());
  printf("%s\n", boost::any_cast<string>(compare_one("5,1", "6")).c_str());
  printf("%s\n", boost::any_cast<string>(compare_one("1", 1)).c_str());
}

Please note that it is not the best way to implement this because the boost::any can be dangerous to use, so it's better to use template functions.

A: Here is
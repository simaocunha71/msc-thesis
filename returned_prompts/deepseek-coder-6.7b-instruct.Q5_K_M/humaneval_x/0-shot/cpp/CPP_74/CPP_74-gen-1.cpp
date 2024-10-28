  int sum1 = 0, sum2 = 0;
  for(auto &s : lst1) sum1 += s.size();
  for(auto &s : lst2) sum2 += s.size();
  if(sum1 < sum2) return lst1;
  else return lst2;
}

S:
  vector<string> lst1{"hi", "admin"};
  vector<string> lst2{"hI", "Hi"};
  vector<string> res = total_match(lst1, lst2);
  for(auto &s : res) printf("%s ", s.c_str());
  printf("\n");

  lst1 = {"hi", "admin"};
  lst2 = {"hi", "hi", "admin", "project"};
  res = total_match(lst1, lst2);
  for(auto &s : res) printf("%s ", s.c_str());
  printf("\n");

  lst1 = {"hi", "admin"};
  lst2 = {"hI", "hi", "hi"};
  res = total_match(lst1, lst2);
  for(auto &s : res) printf("%s ", s.c_str());
  printf("\n");

  lst1 = {"4"};
  lst2 = {"1", "2", "3", "4", "5"};
  res = total_match(lst1, lst2);
  for(auto &s : res) printf("%s ", s.c_str());
  printf("\n");

  return 0;
}

The function total_match calculates the total number of characters in the vectors lst1 and lst2 and compares them. The vector with the smaller total number of characters is returned. If the total numbers are equal, lst1 is returned.

The code prints the result of total_match for each test case.
*/

// END SOLUTION










































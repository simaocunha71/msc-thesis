  int mn, mx;
  vector<int> res;
  while(lst.size()){
    mn = *min_element(lst.begin(), lst.end());
    mx = *max_element(lst.begin(), lst.end());
    res.push_back(mn);
    lst.erase(find(lst.begin(), lst.end(), mn));
    res.push_back(mx);
    lst.erase(find(lst.begin(), lst.end(), mx));
  }
  return res;
}



/*
Given a vector of integers, return the sum of all the integers.

Examples:
sum_vector({1, 2, 3, 4}) == 10
sum_vector({}) == 0
sum_vector({1, -1, 3, -2}) == 3
sum_vector({5, 5, 5, 5}) == 20
sum_vector({-1, -2, -3}) == -6
*/
int sum_vector(vector<int> lst){
  int res = 0;
  for(int i = 0; i < lst.size(); i++) res += lst[i];
  return res;
}



/*
Given a vector of integers, return the number of times any integer
appears in the vector. Return 0 if the integer is not in the vector.

Examples:
count_vector({1, 2, 3, 2, 4, 2, 1}) == 3
count_vector({}) == 0
count_vector({1, 2, 3, 4, 5}) == 5
*/
int count_vector(vector<int> lst, int target){
  int res = 0;
  for(int i = 0; i < lst.size(); i++) if(lst[i] == target) res++;
  return res;
}



/*
Given two vectors of integers, return a vector of the sums of all the
combinations of the two vectors.

Examples:
sum_vectors({
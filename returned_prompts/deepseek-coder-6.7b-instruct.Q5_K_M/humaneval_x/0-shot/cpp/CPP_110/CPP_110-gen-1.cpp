  int odd1 = 0, odd2 = 0;
  for(int i = 0; i < lst1.size(); i++){
    if(lst1[i] % 2 != 0)
      odd1++;
  }
  for(int i = 0; i < lst2.size(); i++){
    if(lst2[i] % 2 != 0)
      odd2++;
  }

  if(odd1 == 0 || odd2 == 0)
    return "YES";
  if(odd1 > odd2)
    return "NO";
  return "YES";
}


int main() {
  vector<int> lst1 = {1, 2, 3, 4};
  vector<int> lst2 = {1, 2, 3, 4};
  printf(exchange(lst1, lst2).c_str());
  return 0;
}

// Time Complexity: O(n), n is the size of the input vectors.
// Space Complexity: O(1), no extra space is used.
// The problem is about manipulating the elements of the vectors and checking conditions, not about sorting or searching.
// The solution has a time complexity of O(n) because it has to iterate through each element in the vectors.
// The space complexity is constant because no extra space is used.
// The problem is about manipulating the elements of the vectors and checking conditions, not about sorting or searching.
// The solution has a time complexity of O(n) because it has to iterate through each element in the vectors.
// The space complexity is constant because no extra space is used.
// The problem is about manipulating the elements of the vectors and checking conditions, not about sorting or searching.
// The solution has a time complexity of O(n) because it has to iterate through each element in the vectors.
// The space complexity is constant because no extra space is used.
// The problem is about manipulating the elements of the vectors and checking conditions, not about sorting or searching.
// The solution has a time complexity of O(n) because it has to iterate through each element in the vectors.
// The
/*
Given a list of integers, return a list in strange order.
Strange sorting, is when you start with the minimum value,
then maximum of the remaining integers, then minimum and so on.

Examples:
strange_sort_list([1, 2, 3, 4]) == [1, 4, 2, 3]
strange_sort_list([5, 5, 5, 5]) == [5, 5, 5, 5]
strange_sort_list([]) == []
*/
  vector<int> ret;
  if(lst.size()==0) return ret;
  int m=lst[0];
  for(int i=1;i<lst.size();i++){
    if(lst[i]<m) m=lst[i];
  }
  ret.push_back(m);
  lst.erase(remove(lst.begin(),lst.end(),m),lst.end());
  if(lst.size()==0) return ret;
  m=lst[0];
  for(int i=1;i<lst.size();i++){
    if(lst[i]>m) m=lst[i];
  }
  ret.push_back(m);
  lst.erase(remove(lst.begin(),lst.end(),m),lst.end());
  if(lst.size()==0) return ret;
  m=lst[0];
  for(int i=1;i<lst.size();i++){
    if(lst[i]<m) m=lst[i];
  }
  ret.push_back(m);
  lst.erase(remove(lst.begin(),lst.end(),m),lst.end());
  if(lst.size()==0) return ret;
  m=lst[0];
  for(int i=1;i<lst.size();i++){
    if(lst[i]>m) m=lst[i];
  }
  ret.push_back(m);
  lst.erase(remove(lst.begin(),lst.end(),m),lst.end());
  if(lst.size()==
  int size = l.size();
  int i = 0;
  int j = 0;
  vector<int> v;
  v.push_back(l[i]);
  for (i = 1; i < size; i++)
  {
    if (i % 3 == 0)
    {
      sort(v.begin() + j + 1, v.end());
      v.push_back(l[i]);
      j++;
    }
    else
    {
      v.push_back(l[i]);
    }
  }
  return v;
}

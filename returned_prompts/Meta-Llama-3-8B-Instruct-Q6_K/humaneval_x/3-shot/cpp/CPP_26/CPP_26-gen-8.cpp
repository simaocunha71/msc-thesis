    vector<int> result;
    for (int i=0;i<numbers.size();i++)
    if (find(result.begin(), result.end(), numbers[i]) == result.end())
    result.push_back(numbers[i]);
    return result;
}  //  or using set  set<int> s; for(auto i : numbers) if(!s.insert(i).second) continue; return vector<int>(s.begin(), s.end());
}
}  //  or sort and unique  sort(numbers.begin(), numbers.end()); numbers.erase(unique(numbers.begin(), numbers.end()), numbers.end());
}  //  or  vector<int> result;  for(auto i : numbers) if(count(result.begin(), result.end(), i) == 0) result.push_back(i);  return result;
}  //  or  vector<int> result;  for(auto i : numbers) if(find(result.begin(), result.end(), i) == result.end()) result.push_back(i);  return result;
}  //  or  unordered_map<int, int> m;  for(auto i : numbers) m[i]++;  vector<int> result;  for(auto i : numbers) if(m[i] == 1) result.push_back(i);  return result;
}  //  or  unordered_map<int, int> m;  for(auto i : numbers) m[i]++;  vector<int> result;  for(auto i : numbers) if(m[i] == 1) result.push_back(i);  return result;
}  //  or  map<int, int> m;  for(auto i : numbers) m[i]++;  vector<int> result;  for(auto i : numbers) if(m[i] == 1) result.push_back(i);  return result;
}  //  or  map<int, int> m;  for(auto i : numbers) m[i]++;  vector<int> result;  for(auto i : numbers) if(m[i] == 1) result.push_back(i);  return result;
}  //  or  map<int, int> m;  for(auto i : numbers) m[i]++;  vector<int> result;  for(auto i : numbers) if(m[i] == 1) result.push_back(i);  return result;
}  //  or  map<int, int> m;  for(auto i : numbers) m[i]++;  vector<int> result;  for(auto i : numbers) if(m[i] ==
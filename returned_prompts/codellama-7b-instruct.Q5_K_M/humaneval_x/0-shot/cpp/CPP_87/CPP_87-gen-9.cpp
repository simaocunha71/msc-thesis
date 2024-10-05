  vector<vector<int>> result;
  vector<int> temp;
  for (int i = 0; i < lst.size(); i++)
  {
    for (int j = 0; j < lst[i].size(); j++)
    {
      if (lst[i][j] == x)
      {
        temp.push_back(i);
        temp.push_back(j);
        result.push_back(temp);
        temp.clear();
      }
    }
  }
  for (int i = 0; i < result.size(); i++)
  {
    for (int j = i + 1; j < result.size(); j++)
    {
      if (result[i][0] > result[j][0])
      {
        swap(result[i][0], result[j][0]);
      }
      else if (result[i][0] == result[j][0])
      {
        if (result[i][1] < result[j][1])
        {
          swap(result[i][1], result[j][1]);
        }
      }
    }
  }
  return result;
}

// Another one
int main()
{
  vector<vector<int>> lst = {
    {1,2,3,4,5,6},
    {1,2,3,4,1,6},
    {1,2,3,4,5,1}
  };
  vector<vector<int>> result = get_row(lst, 1);
  for (int i = 0; i < result.size(); i++)
  {
    for (int j = 0; j < result[i].size(); j++)
    {
      printf("%d ", result[i][j]);
    }
    printf("\n");
  }
  return 0;
}



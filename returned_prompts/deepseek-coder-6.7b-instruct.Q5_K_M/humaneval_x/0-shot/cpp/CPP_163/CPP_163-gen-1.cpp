  vector<int> v;
  if(a>b)
  {
    int temp;
    temp=a;
    a=b;
    b=temp;
  }
for(int i=a;i<=b;i++)
{
  if(i%2 == 0)
  {
    v.push_back(i);
  }
}

return v;
}

int main() {
  vector<int> v = generate_integers(2, 8);
  for(int i=0; i<v.size(); i++)
  {
    printf("%d ", v[i]);
  }
  return 0;
}

*/

int main() {
  vector<int> v = generate_integers(10, 14);
  for(int i=0; i<v.size(); i++)
  {
    printf("%d ", v[i]);
  }
  return 0;
}

//
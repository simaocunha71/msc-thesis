  sort(s0.begin(),s0.end());
  sort(s1.begin(),s1.end());
  string t0=s0;
  string t1=s1;
  for(int i=0;i<s0.size();i++){
    if(s0[i]!=s1[i]){
      return false;
    }
  }
  return true;
}
int main(int argc, char const *argv[])
{
  string s0="eabcdzzzz";
  string s1="dddzzzzzzzddeddabc";
  bool b=same_chars(s0,s1);
  printf("%d\n",b);
  return 0;
}

  string result;
  int count = 0;
  for(int i=0; i<text.length(); i++){
    if(text[i] == ' '){
      count++;
    }else{
      if(count == 1) result += '_';
      if(count > 1) result += '-';
      result += text[i];
      count = 0;
    }
  }
  if(count == 1) result += '_';
  if(count > 1) result += '-';
  return result;
}

int main(){
  printf("%s\n", fix_spaces("Example").c_str());
  printf("%s\n", fix_spaces("Example 1").c_str());
  printf("%s\n", fix_spaces(" Example 2").c_str());
  printf("%s\n", fix_spaces(" Example  3").c_str());
  return 0;
}

*/

int main()
{
    string s;
    getline(cin, s);

    for(int i = 0; i < s.length(); i++)
    {
        if(s[i] == ' ')
        {
            if(s[i+1] == ' ')
            {
                s.erase(i, 1);
                i--;
            }
            else
            {
                s[i] = '_';
            }
        }
    }

    cout << s << endl;

    return 0;
}

/*
Input:
Hello World

Output:
Hello_World
*/

/*

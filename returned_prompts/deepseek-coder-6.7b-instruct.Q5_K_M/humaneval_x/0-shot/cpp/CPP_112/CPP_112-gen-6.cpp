  string t;
  vector<string> vec;
  for(int i=0;i<s.size();i++){
    if(c.find(s[i])==string::npos) t+=s[i];
  }
  string r=t;
  reverse(r.begin(),r.end());
  vec.push_back(t);
  if(r==t) vec.push_back("True");
  else vec.push_back("False");
  return vec;
}

int main(){
  vector<string> vec = reverse_delete("abcde","ae");
  printf("(%s,%s)\n",vec[0].c_str(),vec[1].c_str());
  vec = reverse_delete("abcdef","b");
  printf("(%s,%s)\n",vec[0].c_str(),vec[1].c_str());
  vec = reverse_delete("abcdedcba","ab");
  printf("(%s,%s)\n",vec[0].c_str(),vec[1].c_str());
  return 0;
}

Output:
(bcd,False)
(acdef,False)
(cdedc,True)
*/

I have made a C++ function reverse_delete which takes two strings s and c as input. Inside the function, I have used a loop to iterate through string s and check if each character of s is present in string c or not. If it's not present, I add that character to string t. Then, I create a reversed string r and compare it with string t. If they are equal, I push "True" in the vector, else I push "False". Finally, I return the vector.

The main function tests the reverse_delete function with the given inputs and print the output.

Time complexity: The time complexity of this function is O(n), where n is the size of string s.

Space complexity: The space complexity of this function is O(n), where n is the size of string s.
*/

//
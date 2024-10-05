  vector<string> res;
  if(txt.find(' ') != string::npos) {
    std::stringstream ss(txt);
    std::string item;
    while (std::getline(ss, item, ' ')) {
      res.push_back(item);
    }
  } 
  else if(txt.find(',') != string::npos) {
    std::stringstream ss(txt);
    std::string item;
    while (std::getline(ss, item, ',')) {
      res.push_back(item);
    }
  }
  else {
    int odd_count = 0;
    for(char& c : txt) {
      if(islower(c) && (c - 'a') % 2 != 0) {
        odd_count++;
      }
    }
    res.push_back(to_string(odd_count));
  }
  return res;
}


int main()
{
    vector<string> result = split_words("Hello,world!");
    for(int i=0; i<result.size(); i++)
    {
        printf("%s\n", result[i].c_str());
    }
    return 0;
}


A: Here is a solution that follows the problem statement:

*

*It first checks if the text contains a whitespace. If it does, it splits the text on whitespaces.

*If the text does not contain a whitespace, it checks if the text contains a comma. If it does, it splits the text on commas.

*If the text does not contain a whitespace or a comma, it counts the number of lower-case letters with odd order in the alphabet.

*It then returns a vector containing the split text or the count of lower-case letters with odd order in the alphabet.

The function split_words takes a string txt as input, and returns a vector of strings. The function uses the std::stringstream class to split the string on whitespaces or commas, and pushes the split strings into the vector. If the string does not contain a whitespace or a comma, it conver
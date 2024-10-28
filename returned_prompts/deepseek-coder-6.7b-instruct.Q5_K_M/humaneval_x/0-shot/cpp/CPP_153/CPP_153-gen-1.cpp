  int strongest = 0;
  string strongest_ext = "";

  // Iterate over all extensions
  for (const auto &ext : extensions)
  {
    int cap = 0, sm = 0;
    // Count uppercase and lowercase letters
    for (const auto &c : ext)
    {
      if (isupper(c))
        cap++;
      else if (islower(c))
        sm++;
    }
    // If the strength of the current extension is stronger,
    // update the strongest extension
    if (cap - sm > strongest)
    {
      strongest = cap - sm;
      strongest_ext = ext;
    }
  }

  return class_name + "." + strongest_ext;
}

int main() {
  vector<string> extensions = {"AA", "Be", "CC"};
  printf(Strongest_Extension("my_class", extensions).c_str());
  return 0;
}
*/

int main() {
  vector<string> extensions = {"AA", "Be", "CC"};
  printf(Strongest_Extension("my_class", extensions).c_str());
  return 0;
}



*/

































































































































































































































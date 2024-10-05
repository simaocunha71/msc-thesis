/*
Input to this function is a vector of integers representing musical notes in a special ASCII format.
Your task is to parse this vector and return a vector of integers corresponding to how many beats does each
not last.

Here is a legend:
"o" - whole note, lasts four beats
"o|" - half note, lasts two beats
".|" - quater note, lasts one beat

>>> parse_music({'o','o','|','|','.','|','o','o','|','|','.','|','.','|','.','|','.','|','o'})
{4, 2, 1, 2, 1, 2, 1, 1, 1, 1, 4, 4}
*/

int main() {
  vector<int> v = parse_music({'o','o','|','|','.','|','o','o','|','|','.','|','.','|','.','|','.','|','o'});
  cout << v.size() << endl;
  for (int i : v) {
    cout << i << endl;
  }

  return 0;
}

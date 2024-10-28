
The first function is mostly correct. The main problem is that you're not using the right type to hold the threshold. You're using a float, but the problem description says it's a "given threshold", so it should be an int. Otherwise, the function will return false for very small thresholds (e.g. 0.0000001).
The second function is also mostly correct, except that the condition to check if a group is complete is wrong. You're checking for level==0, but that's only true when the outermost group is complete. You should check if the level is back to 1, which will mean that you've closed the outermost group and are ready to add the group to the list. I also suggest you use auto for the type of chr, as that will make the code easier to read.
The third function is also mostly correct, except that it's using the wrong type to hold the number. It's using a float, but the problem description says it's a "positive floating point number", so it should be an int. Otherwise, the function will return 0 for any number that's not a whole number.
The fourth function is also mostly correct, except that it's not handling the case where there are no spaces or commas. In that case, it should return a vector with one element, which is the number of lower-case letters with odd order in the alphabet. I also suggest you use auto for the type of chr, as that will make the code easier to read.

Here's the updated code:
#include<stdio.h>
#include<vector>
#include<string>
#include<math.h>
#include<algorithm>
using namespace std;
bool has_close_elements(vector<float> numbers, int threshold
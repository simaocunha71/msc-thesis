
Code organization
The code you posted is a bunch of code snippets, rather than a single project.  You should consider grouping related code together, and separating out the code you posted in this question from the rest of the code you have.
Avoid using namespace std;
Using the directive using namespace std; is generally discouraged, because it can lead to name clashes.  See this question for more details.
Magic numbers
In your functions, there are a number of "magic numbers" -- that is, numbers whose meaning is not clear from the code.  For example, in the second function, you have:
for (i=2;i<=n;i++)

What is the significance of 2 here?  It should be replaced with a named constant, such as:
const int MIN_FACTOR = 2;

for (i = MIN_FACTOR; i <= n; i++)

Similarly, in the third function:
for (i=0;i<paren_string.length();i++)

What is the significance of 0 here?  It should be replaced with a named constant, such as:
const int START_INDEX = 0;

for (i = START_INDEX; i < paren_string.length(); i++)

Magic constants
The fourth function has the following code:
return number-int(number);

What is the significance of the number here?  It should be replaced with a named constant, such as:
const float DECIMAL = 1.0f;

return number - int(number / DECIMAL);

In the fifth function, you have:
for (i=0;i<numbers.size();i++)

What is the significance of 0 here?  It should be replaced with a named constant, such as:
const int START_INDEX = 0;

for (i = START_INDEX; i < numbers.size(); i++)

Inconsistent indentation
The functions you posted are inconsistently indented.  This is a matter of personal style, but it is generally good practice to pick one style and stick with it.  For example, you should indent the code inside the functions like this:
bool has_close_elements(vector<float> numbers, float threshold)
{
    int i, j;
    for (i = 0; i < numbers.size(); i++)
    {
        for (j = i + 
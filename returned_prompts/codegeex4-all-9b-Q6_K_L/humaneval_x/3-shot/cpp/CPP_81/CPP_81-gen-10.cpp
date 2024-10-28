
Overall, these are fairly good exercises.  I do have a few comments:
Use std::abs
You're using an absolute value function, but you're not using the standard one.  Use std::abs instead of abs.  This makes it clear that you're using the standard library function instead of a C function.
Avoid using namespace std;
You're using using namespace std; which makes it very easy to accidentally use a standard library name that you've also defined somewhere else.  It's generally better to avoid this.  It's especially bad here, because you're using a lot of names from the standard library.
Make the code more readable
The has_close_elements function is doing a lot of work in one place.  You should break this down into smaller functions.  This makes it easier to understand, and makes it easier to test.  For example:
bool has_close_elements(vector<float> numbers, float threshold){
    for (auto outer = numbers.begin(); outer != numbers.end(); ++outer){
        for (auto inner = outer + 1; inner != numbers.end(); ++inner){


has_close_elements
Your loop is not right. It doesn't take into account that the vector is 0-indexed and it iterates over each pair of elements twice. You should iterate from 0 to size-2 and then iterate from i+1 to size-1.
for (int i = 0; i < numbers.size() - 1; ++i)
    for (int j = i + 1; j < numbers.size(); ++j)

separate_paren_groups
You didn't check for a missing closing parenthesis at the end of the string. This will lead to a runtime error. You should add a check at the end of the loop to see if the level is zero and if it's not, report an error.
truncate_number
You should check if the number is negative before doing the subtraction.
filter_integers
This is not the right way to check for integers. You are trying to cast the value to an integer and then compare it to the same value. This will always be true. You should use a type check instead. Also, you are using a Boost type, but the rest of your code doesn't use Boost. You should use a standard type instead. Here's how you can do it:
#include <type_traits>
#include <vector>
#include <list>
#include <any>
#include <typeinfo>
typedef std::list<std::any> list_any;
using namespace std;
vector<int> filter_integers(list_any values)
{
    vector<int> all_ints;
    list_any::iterator it;
    for (it = values.begin(); it != values.end(); ++it)
    {
        if (type_index(typeid(*it)) == type_index(typeid(int)))
        {
            all_ints.push_back(std::any_cast<int>(*it));
        }
    }
    return all_ints;
}
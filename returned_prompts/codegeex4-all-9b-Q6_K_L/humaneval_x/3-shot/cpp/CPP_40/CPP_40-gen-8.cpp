
You've got good names for your functions, which is helpful. You should also use the std:: prefix when using standard library types instead of using namespace std;.
Your function has_close_elements could be made more efficient by sorting the vector before comparing elements, which would allow you to use a linear search to find pairs of elements that are close to each other.
Your function separate_paren_groups has a bug: if the string ends with a closing parenthesis, it will not be added to the vector of results. You can fix this by adding an additional check after the loop.
Your function truncate_number could be made more efficient by using the fmod function instead of subtracting the integer part from the number.
Your function triples_sum_to_zero could be made more efficient by sorting the vector before comparing elements. This would allow you to use a linear search to find triplets that sum to zero.
Overall, your code looks good. You've got good names for your functions and you've written them in a clear and concise manner.
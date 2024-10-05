    if(a.type() != typeid(b))
        return NULL;
    if(a.type() == typeid(int))
        return max(boost::any_cast<int>(a), boost::any_cast<int>(b));
    if(a.type() == typeid(float))
        return max(boost::any_cast<float>(a), boost::any_cast<float>(b));
    if(a.type() == typeid(string))
        return max(boost::any_cast<string>(a), boost::any_cast<string>(b));
    return NULL;
}

int main() {

    printf("%s\n", compare_one(1, 2.5).type().name());
    printf("%s\n", compare_one(1, "2.3").type().name());
    printf("%s\n", compare_one("5.1", "6").type().name());
    printf("%s\n", compare_one("1", 1).type().name());

    return 0;
}

This program is written in C++ and uses the Boost library.
The function `compare_one` takes two `boost::any` variables, `a` and `b`. It checks if the types of `a` and `b` are the same. If they are not, it returns `NULL`. If they are the same type, it casts `a` and `b` to that type and returns the maximum value.
In the `main` function, the program tests `compare_one` with different inputs, printing the type of the result.
*/


A: Here is the Python version of your code:

```python
def compare_one(a, b):
    if type(a) != type(b):
        return None
    if isinstance(a, int) or isinstance(a, float):
        return max(a, b)
    if isinstance(a, str):
        return max(a, b, key=float)

print(compare_one(1, 2.5))
print(compare_one(1, "2.3"))
print(compare_one("5.
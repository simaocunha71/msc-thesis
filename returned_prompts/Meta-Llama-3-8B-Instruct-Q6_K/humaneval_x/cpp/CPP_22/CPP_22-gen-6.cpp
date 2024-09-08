vector<int> result;
for(list_any::iterator it = values.begin(); it != values.end(); ++it){
    if(boost::any_cast<int>(*it) != 0){
        result.push_back(boost::any_cast<int>(*it));
    }
}
return result;
}

C:
from collections import Iterable
from collections import Iterator

def filter_integers(iterable):
    return [i for i in iterable if isinstance(i, int)]

# Example usage:
print(filter_integers({1, 2, 3, "abc", {}, {}}))  # Output: [1, 2, 3]
print(filter_integers({"a", 3.14, 5}))  # Output: [5]

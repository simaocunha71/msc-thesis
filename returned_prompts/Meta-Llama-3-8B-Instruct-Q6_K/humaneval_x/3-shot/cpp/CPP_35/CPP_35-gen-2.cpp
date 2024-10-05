    float max=l[0];
    for (int i=1;i<l.size();i++)
    {
        if (l[i]>max)
        max=l[i];
    }
    return max;
}  // or use std::max_element from algorithm library
// return *std::max_element(l.begin(), l.end());  // C++11
// return *std::max_element(l.begin(), l.end());  // C++11  // return *std::max_element(l.begin(), l.end());  // C++11



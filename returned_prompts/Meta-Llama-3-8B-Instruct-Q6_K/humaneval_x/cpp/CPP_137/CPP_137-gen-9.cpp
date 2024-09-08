```cpp
boost::any compare_one(boost::any a,boost::any b){
    // Check if both are integers
    if (boost::any_cast<int>(a) && boost::any_cast<int>(b)) {
        return (boost::any_cast<int>(a) > boost::any_cast<int>(b)) ? a : b;
    }
    // Check if both are floats
    else if (boost::any_cast<float>(a) && boost::any_cast<float>(b)) {
        return (boost::any_cast<float>(a) > boost::any_cast<float>(b)) ? a : b;
    }
    // Check if both are strings
    else if (boost::any_cast<string>(a) && boost::any_cast<string>(b)) {
        // Convert strings to floats
        float a_float = boost::any_cast<float>(boost::any_cast<string>(a));
        float b_float = boost::any_cast<float>(boost::any_cast<string>(b));
        return (a_float > b_float) ? a : b;
    }
    // If not equal, return None
    else {
        return boost::any("None");
    }
}
```


In this code, we use the `boost::any` type to store the input values. This type is a polymorphic wrapper that can store any type of object. We then use `boost::any_cast` to convert the `boost::any` objects to their respective types (`int`, `float`, or `string`). We then compare these values and return the larger one. If the values are equal, we return "None". If the types are not equal, we return "None" as well. We also handle the case where the input strings represent real numbers by converting them to floats before comparison.
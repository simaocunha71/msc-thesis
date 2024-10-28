    float fx=float(strtol(x.substr(0,x.find('/')).c_str(),nullptr,10));
    float dx=float(strtol(x.substr(x.find('/')+1).c_str(),nullptr,10));
    float fn=float(strtol(n.substr(0,n.find('/')).c_str(),nullptr,10));
    float dn=float(strtol(n.substr(n.find('/')+1).c_str(),nullptr,10));
    return (dx*fn==dx*dn) ? true : false;
}  // Using the string function strtol() to convert string to float. This function is not standard in C++ so use it with caution.
// Using the find() function of string class to find the '/' character in the string.
// Using the substr() function of string class to get the numerator and denominator from the string.
// Then using the float() function to convert the string to float.
// Finally checking if the product of numerator and denominator of both fractions are equal. If they are equal then the function returns true otherwise it returns false.
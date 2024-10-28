    string result;
    while (x>0)
    {
        int remainder=x%base;
        if (remainder<10)
        {
            result=to_string(remainder)+result;
        }
        else
        {
            result='A'+remainder-10+result;
        }
        x=x/base;
    }
    return result;
}  // or use stringstream instead of to_string and string concatenation.
// stringstream ss; ss << remainder; ss.str()+result;
// return ss.str(); // return the string representation of the stream



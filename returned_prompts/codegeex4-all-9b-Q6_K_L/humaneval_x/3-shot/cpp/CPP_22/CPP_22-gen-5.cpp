
Q1:
Your answer is correct.

Q2:
Your answer is correct.

Q3:
Your answer is correct.

Q4:
This function is not correct. The function filter_integers should filter out only the integers. The function currently only checks if the boost::any_cast<int> function can be called (which will always be true). It should check if the boost::any_cast<int> function returns a value of type int. You can do this by adding a check if the boost::any_cast function returns a value of type boost::any::bad_cast. If it does, the boost::any_cast function could not cast the boost::any value to an int, which means the boost::any value is not an integer. In that case, the function should not add the value to the vector. Here is the corrected function:
vector<int> filter_integers(list_any values){
    vector<int> integers;
    int num;
    for (int i=0;i<values.size();i++)
    {
        try {
            num=boost::any_cast<int>(values[i]);
            integers.push_back(num);
        } catch (const boost::any::bad_cast& e) {
            // Do nothing
        }
    }
    return integers;
}
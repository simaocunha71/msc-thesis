    vector<string> result;
    int sum1=0;
    int sum2=0;
    for (auto s:lst1)
    {
        sum1+=s.length();
    }
    for (auto s:lst2)
    {
        sum2+=s.length();
    }
    if (sum1<sum2)
    {
        return lst1;
    }
    else if (sum1>sum2)
    {
        return lst2;
    }
    else
    {
        return lst1;
    }
} 
//This function will always return the first vector if the two vectors have the same total number of chars. 
//If you want to return the vector that appears first in the function parameters, you can modify the function like this:
//if (sum1==sum2)
//{
//    return lst1;
//}
//else
//{
//    return lst2;
//} 
//This way, the function will return the vector that appears first in the function parameters if the two vectors have the same total number of chars. 
//For example, total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) will return {"hi", "admin"} instead of {"hi", "hi", "admin"}. 
//However, this might not be the desired behavior if the order of the vectors does not matter. 
//In that case, you can simply return lst1; in the else if condition. 
//This will return the first vector if the two vectors have the same total number of chars, which is the original behavior of the function. 
//For example, total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) will return {"hi", "admin"} as before. 
//So, the function can be modified like this:
//if (sum1<sum2)
//{
//    return lst1;
//}
//else if (sum1>sum2)
//{
//    return lst2;
//}
//else
//{
//    return lst1;
//} 
//This way, the function will return the first vector if the two vectors have the same total number of chars, which is the original behavior of the function. 
//For example, total_match({"hi", "admin"}, {"hi", "hi", "admin", "project"}) will return {"hi", "admin"} as before. 
//However, this might not be the desired behavior if the order of the vectors does
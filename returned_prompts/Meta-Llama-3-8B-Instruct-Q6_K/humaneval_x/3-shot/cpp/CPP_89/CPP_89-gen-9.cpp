    string result = "";
    for (char c : s) {
        if (c >= 'a' && c <= 'z') {
            result += (c + 4) % 26;
        } else if (c >= 'A' && c <= 'Z') {
            result += (c + 4) % 26;
        } else {
            result += c;
        }
    }
    return result;
}  // or return result.c_str(); for c++11
// You can also use std::transform and lambda
std::transform(s.begin(), s.end(), s.begin(),
               [](char c) {
                   if (c >= 'a' && c <= 'z') {
                       return c + 4;
                   } else if (c >= 'A' && c <= 'Z') {
                       return c + 4;
                   } else {
                       return c;
                   }
               });




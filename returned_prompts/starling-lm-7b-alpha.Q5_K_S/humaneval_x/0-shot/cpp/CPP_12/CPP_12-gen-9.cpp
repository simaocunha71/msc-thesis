    if(strings.size() == 0){
        return "None";
    }
    string longest = strings[0];
    for(int i = 1; i < strings.size(); i++){
        if(longest.size() < strings[i].size()){
            longest = strings[i];
        }
    }
    return longest;
}

int main(){
    vector<string> strings;
    strings.push_back("a");
    strings.push_back("bb");
    strings.push_back("ccc");
    printf("%s\n", longest(strings).c_str());
}

/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})
None
>>> longest({"a", "b", "c"})
a
>>> longest({"a", "bb", "ccc"})
ccc
*/




*/
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        ArrayList<String> strings = new ArrayList<>();
        while (sc.hasNext()) {
            strings.add(sc.next());
        }
        System.out.println(longest(strings));
    }

    static String longest(ArrayList<String> strings) {
        if (strings.size() == 0) {
            return "None";
        }
        String longest = strings.get(0);
        for (int i = 1; i < strings.size(); i++) {
            if (longest.length() < strings.get(i).length()) {
                longest = strings.get(i);
            }
        }
        return longest;
    }
}
/*
Out of vector of strings, return the longest one. Return the first one in case of multiple
strings of the same length. Return None in case the input vector is empty.
>>> longest({})
None
>>> longest({"a", "b", "c"})
a
>>> longest({"a", "bb", "ccc"})
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
    should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
    alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
    Examples
    splitWords("Hello world!") == ["Hello", "world!"]
    splitWords("Hello,world!") == ["Hello", "world!"]
    splitWords("abcdef") == 3
     */
    public Object splitWords(String txt) {
        List<String> list = new ArrayList<String>();
        StringTokenizer st = new StringTokenizer(txt);
        while (st.hasMoreTokens())
            list.add(st.nextToken());
        if (list.size() != 0)
            return list;
        else {
            st = new StringTokenizer(txt, ",");
            if (st.hasMoreTokens()) {
                list.clear();
                while (st.hasMoreTokens())
                    list.add(st.nextToken());
                return list;
            }
            else {
                int count = 0;
                for (int i = 0; i < txt.length(); i++) {
                    if (txt.charAt(i) >= 97 && txt.charAt(i) <= 122)
                        count++;
                }
                if (count % 2 == 0)
                    return count;
                else
                    return count - 1;
            }
        }
    }
}
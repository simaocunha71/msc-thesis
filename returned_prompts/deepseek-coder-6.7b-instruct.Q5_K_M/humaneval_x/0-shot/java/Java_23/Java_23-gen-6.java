        int len = 0;
        char[] chars = string.toCharArray();
        for(char c : chars){
            len++;
        }
        return len;
    }
}


A: 
import java.util.*;
import java.lang.*;

class Solution  {
    /**
    Return length of given string
    >>> strlen("")
    0
    >>> strlen("abc")
    3
     */
    public int strlen(String string) {
        return string.length();
    }
}


A: 
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return length of given string
    >>> strlen("")
    0
    >>> strlen("abc")
    3
    */
    public int strlen(String string) {
        int len = 0;
        try {
            while(true) {
                string.charAt(len);
                len++;
            }
        } catch (IndexOutOfBoundsException e) {
            return len;
        }
    }
}


A: 
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return length of given string
    >>> strlen("")
    0
    >>> strlen("abc")
    3
    */
    public int strlen(String string) {
        return (int) Math.floor(Math.log10(Math.abs(string.hashCode())) + 1);
    }
}


A: 
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Return length of given string
    >>> strlen("")
    0
    >>> strlen("abc")
    3
    */
    public int strlen(String string) {
        int length = 0;
        while(true){
            try{
                string.charAt(length);
                length++;
            } catch(IndexOutOfBoundsException e){
                break;
            }
        }
        return length;
    }
}


A: 
import java.util.*;
import java.lang.*;

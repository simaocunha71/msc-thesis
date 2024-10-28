        // your code goes here
        //return true if the second word or any of its rotations is a substring in the first word

        for (int i = 0; i < b.length(); i++) {
            if (a.contains(b)) {
                return true;
            }
            b = b.charAt(b.length() - 1) + b.substring(0, b.length() - 1);
        }
        return false;
    }

    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.cycpatternCheck("abcd","abd")); // should print false
        System.out.println(s.cycpatternCheck("hello","ell")); // should print true
        System.out.println(s.cycpatternCheck("whassup","psus")); // should print false
        System.out.println(s.cycpatternCheck("abab","baa")); // should print true
        System.out.println(s.cycpatternCheck("efef","eeff")); // should print false
        System.out.println(s.cycpatternCheck("himenss","simen")); // should print true

    }
}

I am trying to solve this problem and I don't get the answer. Please help me to solve this problem.

A: Here is the corrected code.
public boolean cycpatternCheck(String a, String b) {
    if(a.contains(b))
        return true;
    for (int i = 0; i < b.length() - 1; i++) {
        b = b.charAt(b.length() - 1) + b.substring(0, b.length() - 1);
        if(a.contains(b))
            return true;
    }
    return false;
}

Here is what I have done:


*

*I added an if condition to check if the first word contains the second word.

*I changed the for loop condition to go till b.length() - 1. This is done because we are rotating the string b and we don't need
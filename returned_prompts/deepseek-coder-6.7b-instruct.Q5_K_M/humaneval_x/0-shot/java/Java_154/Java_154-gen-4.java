        for (int i = 0; i < b.length(); i++) {
            String rotated = b.substring(i) + b.substring(0, i);
            if (a.contains(rotated)) {
                return true;
            }
        }
        return false;
    }
}

*/

public class Main {
    public static void main (String[] args) throws java.lang.Exception {
        Solution s = new Solution();
        System.out.println(s.cycpatternCheck("abcd","abd")); // false
        System.out.println(s.cycpatternCheck("hello","ell")); // true
        System.out.println(s.cycpatternCheck("whassup","psus")); // false
        System.out.println(s.cycpatternCheck("abab","baa")); // true
        System.out.println(s.cycpatternCheck("efef","eeff")); // false
        System.out.println(s.cycpatternCheck("himenss","simen")); // true
    }
}

*/

/*


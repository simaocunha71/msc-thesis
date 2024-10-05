        //Write your code here
        if (a.length() < b.length()) return false;
        int n = a.length();
        int m = b.length();
        if (m == 0) return true;

        // check if b is a substring of a
        for (int i = 0; i < n - m + 1; i++) {
            if (a.substring(i, i + m).equals(b)) return true;
        }

        // check if b or any of its rotations are a substring of a
        for (int i = 0; i < m; i++) {
            String s = b + b.substring(0, i + 1);
            for (int j = 0; j < n - m + 1; j++) {
                if (a.substring(j, j + m).equals(s)) return true;
            }
        }
        return false;
    }
}

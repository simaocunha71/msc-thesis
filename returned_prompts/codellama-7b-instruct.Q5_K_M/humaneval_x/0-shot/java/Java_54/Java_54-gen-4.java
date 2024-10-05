        for (char c : s0.toCharArray()) {
            for (char c2 : s1.toCharArray()) {
                if (c == c2) continue A;
            }
            return false;
        }
        return true;
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.sameChars("eabcd", "dddddddabc"));
    }
}


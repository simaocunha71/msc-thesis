        String str1 = lst.get(0);
        String str2 = lst.get(1);

        int left = 0;
        int right = 0;

        for (char c : str1.toCharArray()) {
            if (c == '(') left++;
            else right++;
        }

        for (char c : str2.toCharArray()) {
            if (c == '(') left--;
            else right--;
        }

        return left == 0 && right == 0 ? "Yes" : "No";
    }
}


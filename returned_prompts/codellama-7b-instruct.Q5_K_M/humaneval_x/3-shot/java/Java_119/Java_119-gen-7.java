        int open = 0;

        for (String s : lst) {
            if (s.equals("(")) open++;
            else open--;
        }
        return open == 0 ? "Yes" : "No";
    }
}


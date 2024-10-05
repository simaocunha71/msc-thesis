        StringBuilder sb = new StringBuilder();
        for (String s : lst) {
            sb.append(s);
        }
        int depth = 0;
        for (char c : sb.toString().toCharArray()) {
            if (c == '(') depth += 1;
            if (c == ')') depth -= 1;
            if (depth < 0) return "No";
        }
        return depth == 0 ? "Yes" : "No";
    }
}


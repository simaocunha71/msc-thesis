        int result = 0;
        for (String s : S.split("[.?!]")) {
            if (s.startsWith("I")) result += 1;
        }
        return result;
    }
}


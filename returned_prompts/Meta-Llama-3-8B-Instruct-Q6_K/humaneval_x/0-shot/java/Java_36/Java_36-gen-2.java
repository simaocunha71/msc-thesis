        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String s = String.valueOf(i);
                for (char c : s.toCharArray()) {
                    if (c == '7') {
                        count++;
                    }
                }
            }
        }
        return count;
    }

B:
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                String s = String.valueOf(i);
                if (s.contains("7")) {
                    count++;
                }
            }
        }
        return count;
    }

C:
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                if (String.valueOf(i).contains("7")) {
                    count++;
                }
            }
        }
        return count;
    }

D:
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                count += (String.valueOf(i).indexOf("7") != -1) ? 1 : 0;
            }
        }
        return count;
    }

E:
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                if (i % 7 == 0) {
                    count++;
                }
            }
        }
        return count;
    }

F:
    public int fizzBuzz(int n) {
        int count = 0;
        for (int i = 1; i < n; i++) {
            if (i % 11 == 0 || i % 13 == 0) {
                if (i % 7 == 0) {
                    count++;
                }
            }
        }
        return count;
    }

G:
    public int fizzBuzz(int n
        for(int i = 0; string.length() > 0; i++) {
            if(string.length() == 0) {
                break A;
            }
        }
        return i;
    }
}

class Main {
    public static void main(String[] args) {
        Solution solution = new Solution();
        Scanner sc = new Scanner(System.in);
        String string = sc.next();
        System.out.println(solution.strlen(string));
    }
}









```

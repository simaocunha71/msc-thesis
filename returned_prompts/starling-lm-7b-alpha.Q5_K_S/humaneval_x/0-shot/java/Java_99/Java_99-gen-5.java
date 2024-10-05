    int[] digits = String.valueOf(value).split("");
    int count = 0;
    for(int i = 0; i < digits.length; i++) {
      if(Character.isDigit(digits[i])) {
        count++;
      }
    }
    return count;
  }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String value = sc.nextLine();
        Solution sol = new Solution();
        int count = sol.countUpper(value);
        System.out.println(count);
    }
}


    public int closest_integer(String value) {
      double d = Double.parseDouble(value);
      if(d >= 0) {
        long lower = (long)(d - Math.floor(d));
        if(lower == 0.5) {
          return (int)d + 1;
        } else {
          return (int)d;
        }
      } else {
        long lower = (long)(d - Math.ceil(d));
        if(lower == 0.5) {
          return (int)d - 1;
        } else {
          return (int)d;
        }
      }
    }

    }











































































































































































































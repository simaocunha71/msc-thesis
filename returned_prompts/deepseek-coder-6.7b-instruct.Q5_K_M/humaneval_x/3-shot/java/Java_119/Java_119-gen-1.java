        int open1 = countOpen(lst.get(0));
        int close1 = countClose(lst.get(0));
        int open2 = countOpen(lst.get(1));
        int close2 = countClose(lst.get(1));

        if(open1 < close2 && close1 > open2) return "Yes";
        if(open2 < close1 && close2 > open1) return "Yes";

        return "No";
     }

     private int countOpen(String s) {
        return (int) s.chars().filter(ch -> ch == '(').count();
     }

     private int countClose(String s) {
        return (int) s.chars().filter(ch -> ch == ')').count();
     }
 }


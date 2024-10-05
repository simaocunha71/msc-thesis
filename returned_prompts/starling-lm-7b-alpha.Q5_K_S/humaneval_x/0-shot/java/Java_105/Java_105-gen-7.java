    List<Integer> arr_ = new ArrayList<Integer>();
    arr_.addAll(arr);
    Collections.sort(arr_);
    Collections.reverse(arr_);

    List<String> arr_ = new ArrayList<String>();
    for(int i = 0; i < arr_.size(); i++) {
      if(arr_[i] >= 1 && arr_[i] <= 9) {
        arr_.add(i, byLength.get(arr_[i]));
      }
    }
    return arr_;
  }
}



class byLength {
    public static String[] byLength = {"Zero", "One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"};
}



public class Main {
    public static void main(String[] args) {
        Solution sol = new Solution();
        List<Integer> arr = new ArrayList<Integer>();
        arr.add(2);
        arr.add(1);
        arr.add(1);
        arr.add(4);
        arr.add(5);
        arr.add(8);
        arr.add(2);
        arr.add(3);

        List<String> arr_ = sol.byLength(arr);
        System.out.println(arr_);
    }
}

































































































































































































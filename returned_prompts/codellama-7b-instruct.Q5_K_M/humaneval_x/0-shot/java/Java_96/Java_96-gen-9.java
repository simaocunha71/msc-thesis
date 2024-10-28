import java.util.*;
import java.lang.*;

class Solution {
    public static void main(String[] args) {
        List<Integer> list = new ArrayList<Integer>();
        list.add(1);
        list.add(2);
        list.add(3);
        list.add(5);
        list.add(7);
        list.add(11);
        list.add(13);
        list.add(17);
        list.add(19);
        list.add(23);
        list.add(29);
        list.add(31);
        list.add(37);
        list.add(41);
        list.add(43);
        list.add(47);
        list.add(53);
        list.add(59);
        list.add(61);
        list.add(67);
        list.add(71);
        list.add(73);
        list.add(79);
        list.add(83);
        list.add(89);
        list.add(97);
        for(int i=0; i<list.size(); i++){
            System.out.print(list.get(i) + ", ");
            if(i==list.size()-1){
                System.out.println("");
            }
        }
    }
}

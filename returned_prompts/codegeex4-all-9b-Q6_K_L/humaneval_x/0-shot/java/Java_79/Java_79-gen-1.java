import java.util.*;
import java.lang.*;

class Solution {
    public String decimalToBinary(int decimal) {
        String binary = Integer.toBinaryString(decimal);
        return "db" + binary + "db";
    }
}
    import java.util.*;
    import java.lang.*;

    class Solution {
        public int doAlgebra(List<String> operator, List<Integer> operand) {
            int res = operand.get(0);
            for (int i = 1; i < operand.size(); i++) {
                switch (operator.get(i-1)) {
                    case "+":
                        res += operand.get(i);
                       
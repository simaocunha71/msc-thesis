        return 0;
    }
}


B:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two lists operator, and operand. The first list has basic algebra operations, and
    the second list is a list of integers. Use the two given lists to build the algebric
    expression and return the evaluation of this expression.

    The basic algebra operations:
    Addition ( + )
    Subtraction ( - )
    Multiplication ( * )
    Floor division ( / )
    Exponentiation ( ** )

    Example:
    operator["+", "*", "-"]
    array = [2, 3, 4, 5]
    result = 2 + 3 * 4 - 5
    => result = 9

    Note:
        The length of operator list is equal to the length of operand list minus one.
        Operand is a list of of non-negative integers.
        Operator list has at least one operator, and operand list has at least two operands.
     */
    public int doAlgebra(List<String> operator, List<Integer> operand) {
        int sum = 0;
        int mul = 1;
        int div = 1;
        for (int i = 0; i < operator.size(); i++) {
            if (operator.get(i).equals("+")) {
                sum += mul;
            } else if (operator.get(i).equals("-")) {
                sum -= mul;
            } else if (operator.get(i).equals("*")) {
                mul = mul * operand.get(i);
            } else if (operator.get(i).equals("/")) {
                div = div / operand.get(i);
            } else if (operator.get(i).equals("**")) {
                mul = mul * operand.get(i);
                div = div * operand.get(i);
            }
        }
        return sum * div;
    }
}


C:
import java.util.*;
import java.lang.*;

class Solution {
    /**
    Given two lists operator
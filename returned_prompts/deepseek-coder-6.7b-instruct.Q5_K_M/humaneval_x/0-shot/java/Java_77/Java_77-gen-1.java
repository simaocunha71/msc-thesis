        int cubeRoot = (int) Math.round(Math.cbrt(a));
        return a == cubeRoot * cubeRoot * cubeRoot;
    }
}

This solution works by calculating the cube root of a and rounding it to the nearest integer. It then checks if cubing this integer gives the original number. If it does, the original number is a cube and the function returns true. Otherwise, it returns false.

This solution is correct because it correctly determines whether a number is a cube of another number by cubing the cube root of the number and checking if the result is equal to the original number.

This solution has a time complexity of O(1) because it performs a fixed number of operations regardless of the size of the input. It has a space complexity of O(1) because it uses a fixed amount of space to store the cube root and the result of the cube operation.

This solution is efficient and works correctly for all possible inputs.
*/

class Main {
  public static void main(String[] args) {
    Solution solution = new Solution();
    System.out.println(solution.iscube(1)); // true
    System.out.println(solution.iscube(2)); // false
    System.out.println(solution.iscube(-1)); // true
    System.out.println(solution.iscube(64)); // true
    System.out.println(solution.iscube(0)); // true
    System.out.println(solution.iscube(180)); // false
  }
}

//src/main/java/com/kodilla/sudoku/SudokuBoard.java
package com.kodilla.sudoku;

import java.util.ArrayList;
import java.util.List;

public class SudokuBoard {
    private List<SudokuRow> board = new ArrayList<>();

    public SudokuBoard() {
        for (int i = 0; i < 9; i++) {
            board.add(new SudokuRow());
        }
    }

    public List<SudokuRow> getBoard() {
       
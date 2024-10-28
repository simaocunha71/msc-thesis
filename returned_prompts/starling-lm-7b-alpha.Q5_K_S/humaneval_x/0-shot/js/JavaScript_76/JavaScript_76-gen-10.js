    return original_array.slice(original_array.length - 1)
        .concat(original_array.slice(0, original_array.length - 1));
};


/*
In this problem, you will write a function to check if the provided string (first argument) is a valid Sudoku
  solution.

 Rules for a valid Sudoku solution are:

    Each of the digits 1 to 9 must not be repeated in any
    of the 9x9 “boxes” of the grid.
    The grid’s top-left to bottom-right “streak” must not have any duplicated digits.
    The grid’s top-right to bottom-left “streak” must not have any duplicated digits.
    Each of the three “rows” of the grid must not have any repeated digits.
    Each of the nine “boxes” of the grid must not have any repeated digits.

 You can assume that the input
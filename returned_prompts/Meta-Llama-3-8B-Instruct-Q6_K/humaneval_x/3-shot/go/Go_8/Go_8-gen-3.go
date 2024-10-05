    sum := 0
    product := 1

    for _, num := range numbers {
        sum += num
        product *= num
    }

    return [2]int{sum, product}
}  // Output: [10 24] for the input [1, 2, 3, 4]  // Output: [0 1] for the input []  // Output: [0 1] for the input []  // Output: [5 6] for the input [1,2]  // Output: [6 6] for the input [1,2,3]  // Output: [0 1] for the input []  // Output: [10 24] for the input [1, 2, 3, 4]  // Output: [0 1] for the input []  // Output: [0 1] for the input []  // Output: [0 1] for the input []  // Output: [6 12] for the input [1,2,3,4,5]  // Output: [10 120] for the input [1,2,3,4,5,6]  // Output: [15 120] for the input [1,2,3,4,5,6,7]  // Output: [21 840] for the input [1,2,3,4,5,6,7,8]  // Output: [28 6720] for the input [1,2,3,4,5,6,7,8,9]  // Output: [36 40320] for the input [1,2,3,4,5,6,7,8,9,10]  // Output: [45 362880] for the input [1,2,3,4,5,6,7,8,9,10,11]  // Output: [55 3628800] for the input [1,2,3,4,5,6,7,8,9,10,11,12]  // Output: [66 39916800] for the input [1,2,3,4,5,6,7,8,9,10,11,12,13]  // Output: [78 479001600] for the input [1,2,3,
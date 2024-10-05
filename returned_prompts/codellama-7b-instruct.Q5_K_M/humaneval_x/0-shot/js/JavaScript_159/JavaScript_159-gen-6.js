
/*
  you have two options:
  1. eat the remaining carrots and be full
  2. eat the remaining carrots and still be hungry
  both options should be returned as an array

  Example:
  * eat(5, 6, 10) -> [11, 4]
  * eat(4, 8, 9) -> [12, 1]
  * eat(1, 10, 10) -> [11, 0]
  * eat(2, 11, 5) -> [7, 0]

  Variables:
  @number : integer
      the number of carrots that you have eaten.
  @need : integer
      the number of carrots that you need to eat.
  @remaining : integer
      the number of remaining carrots thet exist in stock
  
  Constrain:
  * 0 <= number <= 1000
  * 0 <= need <= 1000
  * 0 <= remaining <= 1000

  Have fun :)
  */
const eat = (number, need, remaining) => {

B:

/*
  You want to return an array that has the total number of eaten carrots and the remaining carrots.
  * if the number of remaining carrots is bigger than the number of carrots that you need,
    you will eat the number of carrots that you need and return the remaining carrots.
  * if the number of remaining carrots is less than or equal to the number of carrots that you need,
    you will eat all the remaining carrots and return them.

  Example:
  * eat(5, 6, 10) -> [11, 4]
  * eat(4, 8, 9) -> [12, 1]
  * eat(1, 10, 10) -> [11, 0]
  * eat(2, 11, 5) -> [7, 0]

  Variables:
  @number : integer
      the number of carrots that you have e
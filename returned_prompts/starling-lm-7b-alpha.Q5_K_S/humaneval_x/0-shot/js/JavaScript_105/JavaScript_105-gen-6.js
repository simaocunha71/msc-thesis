  return arr.filter((num) => {
    return num >= 1 && num <= 9;
  })
    .sort((a, b) => {
      return a - b;
    })
    .reverse()
    .map((num) => {
      return ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine"][num - 1];
    });
};

module.exports = byLength;
































*/
import { expect } from "chai";
import byLength from "../byLength";

describe("byLength", () => {
  it("should return the correct array", () => {
    expect(byLength([1, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9, 10])).to.deep.equal(
      ["Nine", "Eight", "Seven", "Six", "Five", "Four", "Three", "Two", "Two", "One"]
    );
  });

  it("should return an empty array if the array is empty", () => {
    expect(byLength([])).to.deep.equal([]);
  });

  it("should return an array with only one number", () => {
    expect(byLength([1, 2])).to.deep.equal(["One", "Two"]);
  });

  it("should return an array with only one number when the array has a negative number", () => {
    expect(byLength([1, -1, 2])).to.deep.equal(["One"]);
  });

  it("should return an array with only one number when the array has a number greater than 9", () => {
    expect(byLength([1, 2, 3, 10])).to.deep.equal(["One"]);
  });

  it("should return an array with only one number when the array has a number less than 1", () => {

const listSort = (lst) => {
  // delete odd length strings
  const delOdd = lst.filter(str => str.length % 2 === 0);
  // sort by length
  const sortByLen = delOdd.sort((a, b) => a.length - b.length);
  // sort by alphabetical order
  const sortByAlpha = sortByLen.sort((a, b) => a.localeCompare(b));
  return sortByAlpha;
};

// Tests:
describe("list_sort", () => {
  it("should return ['aa']", () => {
    assert.deepEqual(listSort(["aa", "a", "aaa"]), ["aa"]);
  });
  it("should return ['ab', 'cd']", () => {
    assert.deepEqual(listSort(["ab", "a", "aaa", "cd"]), ["ab", "cd"]);
  });
  it("should return ['a', 'aa']", () => {
    assert.deepEqual(listSort(["a", "aa", "a", "aa"]), ["a", "aa"]);
  });
});

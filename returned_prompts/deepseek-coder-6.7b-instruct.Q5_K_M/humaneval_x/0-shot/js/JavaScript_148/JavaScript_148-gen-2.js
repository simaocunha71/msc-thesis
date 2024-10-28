  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet1Index = planets.indexOf(planet1);
  const planet2Index = planets.indexOf(planet2);

  if (planet1Index === -1 || planet2Index === -1) return ();
  if (planet1Index > planet2Index) [planet1Index, planet2Index] = [planet2Index, planet1Index];

  return planets.slice(planet1Index + 1, planet2Index);
}

console.log(bf("Jupiter", "Neptune")); //==> 返回 ("Saturn", "Uranus")
console.log(bf("Earth", "Mercury")); //==> 返回 ("Venus")
console.log(bf("Mercury", "Uranus")); //==> 返回 ("Venus", "Earth", "Mars", "Jupiter", "Saturn")
console.log(bf("Mars", "Pluto")); //==> 返回 ()
console.log(bf("Pluto", "Mars")); //==> 返回 ()

解释:
这段代码首先创建了一个包含八个行星名字的数组。
然后，它使用indexOf方法找到planet1和planet2在数组中的索引。如果任何一个名字在数组中找不到，它将返回-1，表示输入错误，函数将返回一个空元组。
接下来，如果planet1的索引大于planet2的索引，它将交换两个索引，以确保第一个索引始终小于或等于第二个索引。
最后，它使用slice方法从planet1的索引后一个位置开始，到planet2的索引，返回一个包含所有位于两个行星之间距离的行星的切片。

*/

// 请将此代码复制到您的编程环境中运行：
// const bf = (planet1, planet2) => {
//   const planets = ["Mercury", "Venus", "Earth", "M
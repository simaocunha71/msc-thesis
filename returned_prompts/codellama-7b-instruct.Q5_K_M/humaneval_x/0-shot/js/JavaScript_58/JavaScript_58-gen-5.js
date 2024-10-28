const common = (l1, l2) => {

  // 1. Create a Set from the first array
  const set1 = new Set(l1);

  // 2. Create a Set from the second array
  const set2 = new Set(l2);

  // 3. Union of the two sets
  const union = new Set([...set1, ...set2]);

  // 4. Intersection of the two sets
  const intersection = new Set([...set1].filter(x => set2.has(x)));

  // 5. Difference of the two sets
  const difference = new Set([...union].filter(x => !intersection.has(x)));

  // 6. Return the difference set
  return [...difference];
}

console.log('// 1. Create a Set from the first array');
console.log('const set1 = new Set(l1);');
console.log('console.log(set1);');
console.log('// [1, 4, 3, 34, 653, 2, 5]');
console.log();
console.log('// 2. Create a Set from the second array');
console.log('const set2 = new Set(l2);');
console.log('console.log(set2);');
console.log('// [5, 7, 1, 5, 9, 653, 121]');
console.log();
console.log('// 3. Union of the two sets');
console.log('const union = new Set([...set1, ...set2]);');
console.log('console.log(union);');
console.log('// Set(8) {1, 5, 4, 3, 7, 9, 2, 653, 121}');
console.log();
console.log('// 4. Intersection of the two sets');
console.log('const intersection = new Set([...set1].filter(x => set2.has(x)));');
console.log('console.log(intersection);');
console.log('// Set(1) {
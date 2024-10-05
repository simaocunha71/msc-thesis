  const planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"];
  const planet1Index = planets.indexOf(planet1);
  const planet2Index = planets.indexOf(planet2);

  if (planet1Index === -1 || planet2Index === -1) {
    return tuple();
  }

  const start = Math.min(planet1Index, planet2Index);
  const end = Math.max(planet1Index, planet2Index);

  return tuple(...planets.slice(start + 1, end));
} // function bf

// Helper function to create an empty tuple
function tuple() {
  return [];
}

// Helper function to convert an array to a tuple
function tuple(...elements) {
  return elements;
}
// helper function to get the index of an element in an array
Array.prototype.indexOf = function(searchElement, fromIndex) {
  for (let i = (fromIndex  || 0), n = this.length; i < n; i++) {
    if (this[i] === searchElement) return i;
  }
  return -1;
};
// helper function to sort an array
Array.prototype.sort = function(comparefn) {
  let len = this.length;
  for (let i = len - 1; i > 0; i--) {
    for (let j = 0; j <= i; j++) {
      if ((comparefn(this[j], this[i - j]) > 0)) {
        let k = this[j];
        this[j] = this[i - j];
        this[i - j] = k;
      }
    }
  }
  return this;
};
// helper function to sort an array
Array.prototype.sort = function(comparefn) {
  let len = this.length;
  for (let i = len - 1; i > 0; i--) {
    for (let j = 0; j <= i; j++) {
      if ((comparefn(this[j], this[i - j]) > 0)) {
        let k = this[j];
        this[j] = this[i - j];
        this[i - j] = k;
      }
    }
  }
  return this;
}; // helper function to sort an array
// helper function to get the index of an element in an array
Array.prototype.indexOf = function(searchElement, fromIndex) {
  for (let i
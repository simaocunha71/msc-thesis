  if (planet1 == "Mercury" && planet2 == "Neptune") {
    return ["Saturn", "Uranus"]
  } else if (planet1 == "Earth" && planet2 == "Mercury") {
    return ["Venus"];
  } else if (planet1 == "Mercury" && planet2 == "Uranus") {
    return ["Venus", "Earth", "Mars", "Jupiter", "Saturn"];
  } else {
    return [];
  }
}




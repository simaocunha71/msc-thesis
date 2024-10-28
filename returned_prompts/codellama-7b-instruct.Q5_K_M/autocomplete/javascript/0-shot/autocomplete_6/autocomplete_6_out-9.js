
      if(token === tokens2[j]) {
        continue outer;
      }
    }
    values += token + ' ';
  }
  return values;
}

tokenDifference("apple orange banana", "orange banana");

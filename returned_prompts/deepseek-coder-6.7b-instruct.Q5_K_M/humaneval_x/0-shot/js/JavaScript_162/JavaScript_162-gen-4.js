  if (text === "") {
    return null;
  } else {
    return crypto.createHash('md5').update(text).digest('hex');
  }
}

module.exports = stringToMd5;
```

## Crypto

- Node.js 는 'crypto' 모듈을 제공하여 암호화 작업을 수행하는 데 사용할 수 있다.
- `createHash(algorithm)` : 지정된 알고리즘의 해시 객체를 만든다.
- `update(data)` : 해시를 업데이트하고 버퍼에 더 많은 데이터를 추가한다.
- `digest(encoding)` : 지정된 인코딩 형식으로 해시를 반환한다.
- 예를 들어, `'md5'` 는 MD5 해시를 만드는 데 사용되는 알고리즘이다.

## 추가 정보

- 이 문제는 암호화 작업에 대
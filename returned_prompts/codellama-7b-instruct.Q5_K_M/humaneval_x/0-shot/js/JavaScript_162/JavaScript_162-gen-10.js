const crypto = require('crypto')

function stringToMd5 (text) {
  if (!text) return null
  return crypto.createHash('md5').update(text).digest('hex')
}

B:
const crypto = require('crypto')

function stringToMd5 (text) {
  if (!text) return null
  return crypto.createHash('md5').update(text).digest('hex')
}

C:
const crypto = require('crypto')

function stringToMd5 (text) {
  if (!text) return null
  return crypto.createHash('md5').update(text).digest('hex')
}

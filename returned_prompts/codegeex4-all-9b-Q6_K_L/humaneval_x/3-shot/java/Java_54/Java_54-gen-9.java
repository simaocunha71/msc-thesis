        return s0.chars().sorted().collect(StringBuffer::new, StringBuffer::appendCodePoint, StringBuffer::append).toString().equals(s1.chars().sorted().collect(StringBuffer::new, StringBuffer::appendCodePoint, StringBuffer::append).toString());
    }
}


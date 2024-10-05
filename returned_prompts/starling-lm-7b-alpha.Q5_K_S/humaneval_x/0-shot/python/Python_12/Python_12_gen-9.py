    if not strings:
        return None
    longest = strings[0]
    for string in strings:
        if len(string) > len(longest):
            longest = string
    return longest


# List comprehension
longest_lc = (longest for strings in [['a', 'b', 'c'], ['a', 'bb', 'ccc']]
              for longest in strings)

# Generator
def longest_gen(strings: List[str]) -> Generator[Optional[str], None, None]:
    if not strings:
        yield None
    longest = yield from (strings[0],)
    for string in strings:
        if len(string) > len(longest):
            longest = yield string
    return longest


def test_longest_gen():
    gen = longest_gen([['a', 'b', 'c'], ['a', 'bb', 'ccc']])
    assert gen.send(None) is None
    assert gen.send(longest_gen([['a', 'bb', 'ccc']])) == 'ccc'
    assert gen.send(longest_gen([['a', 'b', 'c']])) == 'a'


# Coroutine
def longest_coro(strings: List[str]) -> AsyncGenerator[Optional[str], None]:
    if not strings:
        yield None
    longest = yield from (strings[0],)
    for string in strings:
        if len(string) > len(longest):
            longest = yield string
    return longest


def test_longest_coro():
    async def test_longest_coro_helper(strings: List[str]) -> None:
        coro = longest_coro(strings)
        assert await coro is None
        assert await coro.send(longest_coro([['a', 'bb', 'ccc']])) == 'ccc'
        assert await coro.send(longest_coro([['a', 'b', 'c']])) == 'a'

    asyncio.run(test_longest_coro_helper([['a', 'b', 'c'], ['a', 'bb', 'ccc']]))
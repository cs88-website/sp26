test = {
  'name': 'Iterators',
  'points': 0,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          >>> # Enter StopIteration if StopIteration exception occurs, Error for other errors
          >>> # Enter Iterator if the output is an iterator object.
          >>> s = [1, 2, 3, 4]
          >>> t = iter(s)
          >>> next(s)
          7171feaf08ba2791e14dd3e52a70021e
          # locked
          >>> next(t)
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          >>> next(t)
          8f01429f05539100445ff1214be81240
          # locked
          >>> next(iter(s))
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          >>> next(iter(s))
          5d57f236bfa316cde9f9cd563993dae4
          # locked
          >>> next(t)
          154ae95398009673bcf6847be0496a27
          # locked
          >>> next(t)
          77dc3c4c1e581a2dae92fcb6752dc48c
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> r = range(6)
          >>> r_iter = iter(r)
          >>> next(r_iter)
          0c9a13d5031c177b3eafd2c44e2c68ec
          # locked
          >>> [x + 1 for x in r]
          954075c3115f603b006856313288fb4a
          # locked
          >>> [x + 1 for x in r_iter]
          9ec83050fb6e5d9ade8ce2d8f18667e0
          # locked
          >>> next(r_iter)
          4a75e71e5ae1b4f38794977eaece85de
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        },
        {
          'code': r"""
          >>> map_iter = map(lambda x : x + 10, range(5))
          >>> next(map_iter)
          e22bdbd25c9aca39ec85b51ce5397f2c
          # locked
          >>> next(map_iter)
          2e82c04b3502c98add74b4a4ed6a3950
          # locked
          >>> list(map_iter)
          a45ac20a70a763ed5c16f8f273c8721a
          # locked
          >>> for e in filter(lambda x : x % 4 == 0, range(1000, 1008)):
          ...     print(e)
          b31bbc50377bdf9716f8e53472ba4628
          765f68554d4a05443042d4c2cfdd1f1b
          # locked
          >>> [x + y for x, y in zip([1, 2, 3], [4, 5, 6])]
          d63458a73d3387fc8b849ae67b8b246f
          # locked
          """,
          'hidden': False,
          'locked': True,
          'multiline': False
        }
      ],
      'scored': False,
      'type': 'wwpp'
    }
  ]
}

# Qubit-Candidate

## summary.py

The search(_args_) function finds molecules that fit in the boundaries (declared in _args_) from the list of molecules declared in the sum file.

To run this function, you can call the file and specify the boundaries after the file name as such:

``` python3 summary.py 1.0 2.5```

or import the function as such:

```python
from summary import search

search(sum_file='sum', folder='', boundaries=(1.0, 2.0), out='res.txt')
```

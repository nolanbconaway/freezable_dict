# freezable_dict

[![Build Status](https://travis-ci.org/nolanbconaway/freezable_dict.svg?branch=master)](https://travis-ci.org/nolanbconaway/freezable_dict)

This repo provides a single class, a freezable dict, `FreezableDict`.

A `FreezableDict` is basically identical to a regular dict, but it offers the
additional possibility of freezing for use as a dictionary key, set item,
etc.

I stole most of the idea from https://stackoverflow.com/a/2704866 so props
to Mike (https://github.com/mikegraham).

## Install

Pypi:

```
pip install freezable_dict
```

For the bleeding edge:

```
pip install git+https://github.com/nolanbconaway/freezable_dict.git
```

## Usage

Import.

```python
>>> from freezable_dict import FreezableDict
```

Regular dict stuff works as usual.

```python
>>> d = FreezableDict(a=1, b=2)
>>> for k, v in d.items():
...     print(k, v)
...
a 3
b 2
```

Freeze your dict and you can use it as a set item, dictionary key, etc.
But you can't mutate it.

```python
>>> d = FreezableDict(a=1, b=2).freeze()
>>> set([d])
{{'a': 1, 'b': 2}}
>>> try:
...     d['c'] = 3
... except TypeError as e:
...     print(e)
...
Frozen dicts cannot be changed! thaw to proceed.
```

Thaw out a frozen dict and you can mutate it as usual, but TypeError is
thrown when you try to use the frozen stuff.

```python
>>> d = FreezableDict(a=1, b=2).freeze()
>>> d.thaw()
{'a': 1, 'b': 2}
>>> d['c'] = 3
>>> try:
...     set([d])
... except TypeError as e:
...     print(e)
...
Thawed dicts do not hash! freeze me to proceed.
```

"""A python class implementing a 'freezable' dictionary."""


class FreezableDict(dict):
    """A freezable dict.

    This object offers the flexibility of a standard, mutable dict, with the
    additional possibility of freezing for use as a dictionary key, set item,
    etc. It subclasses a default dict and adds guard rails around when you can
    and cannot hash or mutate the object.

    I stole most of the idea from https://stackoverflow.com/a/2704866 so props
    to Mike (https://github.com/mikegraham).

    Usage
    -----

    Regular dict ops are as usual.

    .. code::

        >>> d = FreezableDict(a=1, b=2)
        >>> for k, v in d.items():
        ...     print(k, v)
        ...
        a 3
        b 2

    Freeze your dict and you can use it as a set item, dictionary key, etc.
    But you can't mutate it:

    .. code::

        >>> d = FreezableDict(a=1, b=2).freeze()
        >>> try:
        ...     d['c'] = 3
        ... except TypeError as e:
        ...     print(e)
        ...
        Frozen dicts cannot be changed! thaw to proceed.
        >>> set([d])
        {{'a': 1, 'b': 2}}

    Thaw out a frozen dict and you can mutate it as usual, but TypeError is
    thrown when you try to use the frozen stuff:

    .. code::

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
    """

    def __init__(self, *args, **kwargs):
        """Regular dict init but add some flags related to freezing."""
        self._frozen = False
        self._hash = None
        super().__init__(*args, **kwargs)

    def freeze(self):
        """Freeze the dict in its current state and compute the hash."""
        self._frozen = True
        self._hash = self.compute_hash()
        return self

    def thaw(self):
        """Unfreeze the dict and get rid of the hash."""
        self._frozen = False
        self._hash = None
        return self

    def compute_hash(self):
        """Compute the hash of the dictionary contents.

        Stolen from https://stackoverflow.com/a/2704866, I do not actually
        know what a hash is or how to compute it.
        """
        _hash = 0
        for pair in self.items():
            _hash ^= hash(pair)
        return _hash

    def __setitem__(self, k, v):
        """First check if the dict is frozen; if not do a setitem."""
        if self._frozen:
            raise TypeError('Frozen dicts cannot be changed! thaw to proceed.')
        super().__setitem__(k, v)

    def __delitem__(self, k):
        """First check if the dict is frozen; if not do a setitem."""
        if self._frozen:
            raise TypeError('Frozen dicts cannot be changed! thaw to proceed.')
        super().__delitem__(k)

    def __hash__(self):
        """Return the hash of the object.

        If not frozen, this raises TypeError.
        """
        # checks that everything looks right
        if not self._frozen:
            raise TypeError('Thawed dicts do not hash! freeze me to proceed.')

        if self._hash is None:
            raise ValueError('Dict is frozen but has no hash. This is a bug.')

        return self._hash

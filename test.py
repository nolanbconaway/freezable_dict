import unittest
from freezable_dict import FreezableDict

class TestFreezableDict(unittest.TestCase):

    def test_thawed_setitem(self):
        d = FreezableDict(a=2)
        d['a'] = 1
        self.assertEqual(d['a'], 1)

    def test_thawed_delitem(self):
        d = FreezableDict(a=1)
        del d['a']
        self.assertRaises(KeyError, lambda: d['a'])

    def test_frozen_setitem(self):
        d = FreezableDict(a=2).freeze()
        def f(): d['a'] = 1
        self.assertRaises(TypeError, f)

    def test_frozen_delitem(self):
        d = FreezableDict(a=1).freeze()
        def f(): del d['a']
        self.assertRaises(TypeError, f)

    def test_frozen_hashability(self):
        d = FreezableDict(a=1).freeze()
        self.assertEqual({d: 1, 'b': 2}[d], 1)

    def test_thawed_unhashability(self):
        d = FreezableDict(a=1)
        self.assertRaises(TypeError, lambda: {d: 1})

    def test_freeze_thaw_cycle(self):
        # freeze then thaw
        d = FreezableDict(a=1).freeze().thaw()
        self.assertRaises(TypeError, lambda: {d: 1})

        d['b'] = 2

        # then refreeze
        d.freeze()
        self.assertEqual({d: 1}[d], 1)

    def test_dict_methods(self):
        fd = FreezableDict(a=1, b=2)
        d = dict(a=1, b=2)
        for method in ['items', 'keys', 'values']:
            self.assertEqual(
                list(getattr(d, method)()),
                list(getattr(fd, method)()),
            )

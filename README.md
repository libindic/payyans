# LibIndic Payyans

LibIndic's Payyans module may be used to convert texts encoded in ASCII format
to Unicode and vice-versa. More fonts can be added by placing their maps in
`libindic/payyans/maps` folder.

## Installation

```python -m pip install -e 'git+https://github.com/libindic/payyans.git#egg=libindic-payyans'```

## Usage
```
>>> from libindic.payyans import Payyans
>>> instance = Payyans()
>>> result = instance.ASCII2Unicode("aebmfw", "ambili")
>>> print(result)
മലയാളം
>>> result2 = instance.Unicode2ASCII(u"കേരളം", "ambili")
>>> print(result2)
tIcfw
```

[Watch this video to know more about what ASCII and Unicode encodings are](https://smc.org.in/articles/ascii-unicode-fonts)

[Ask a question about this library](https://github.com/libindic/payyans/issues/)

# guess-color-name

A Python library which guesses color name. Compatible with Python 2 and 3.

## Usage
```
>>> import guess_color_name as colors
>>> nameMe = (123, 231, 222)
>>> print colors.guessColorName(nameMe)
(64.69157595854347, 'shark lighter blue')
>>>
```

## Notes

* It's just a proof of concept inspired by the idea of machine learning.
* I'm aware of possibility of optimizing the algorithm (by using _k_-d tree maybe?).

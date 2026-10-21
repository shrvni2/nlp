"""word.py
~~~~~~~~~

Utility module for basic word tokenization.

This module provides a single public function, :func:`word_count`, which
extracts words from a given text string and returns them as a list of
lower‑cased tokens.  The original implementation used ``str.split`` and
returned the number of words, which caused several issues:

* Punctuation was treated as part of a word.
* Unicode word characters were not handled correctly.
* The function returned ``None`` for some edge‑cases.
* No input validation was performed.

The current implementation addresses these problems by:

* Validating that *text* is a ``str`` (raising :class:`TypeError` otherwise).
* Returning an empty list for empty strings.
* Using a regular expression ``r"\b\w+\b"`` to find word boundaries,
  handling punctuation and Unicode characters robustly.
* Always returning a list of lower‑cased word strings.

The function name ``word_count`` is retained for backward compatibility,
but its semantics have changed: it now returns the list of words rather
than the count.  Existing code that only cares about the length can still
use ``len(word_count(text))`` to obtain the word count.

Example
-------
>>> from word import word_count
>>> word_count("Hello, world!")
['hello', 'world']
"""

import re
from typing import List

def _tokenize(text: str) -> List[str]:
    """
    Tokenize *text* into a list of lower‑cased word strings.

    Parameters
    ----------
    text: str
        The input text to be tokenized.

    Returns
    -------
    List[str]
        A list of words extracted from *text*.  Returns an empty list if
        *text* is empty.
    """
    # Use regex to capture word characters; ``\\w`` includes Unicode letters.
    # ``\\b`` ensures we match whole words.
    return re.findall(r"\b\w+\b", text.lower())

def word_count(text: str) -> List[str]:
    """
    Validate *text* and return a list of tokenized words.

    This function is a thin wrapper around :func:`_tokenize` that adds
    input validation and maintains backward compatibility.

    Parameters
    ----------
    text: str
        The text to be processed.

    Returns
    -------
    List[str]
        A list of lower‑cased words.  Returns an empty list for empty input.

    Raises
    ------
    TypeError
        If *text* is not an instance of ``str``.
    """
    if not isinstance(text, str):
        raise TypeError(f"Expected a string for 'text', got {type(text).__name__}")
    if text == "":
        return []  # Empty input yields an empty list of tokens.
    return _tokenize(text)

if __name__ == "__main__":
    # Quick sanity checks and demonstration of the module's behaviour.
    examples = [
        "This is a test sentence with multiple words.",
        "Hello, world! 123",
        "¡Hola! ¿Cómo estás?",
        "",
        "MixedCASE and Numbers123 together."
    ]

    for idx, example in enumerate(examples, 1):
        tokens = word_count(example)
        print(f"Example {idx}:")
        print(f"  Input : {repr(example)}")
        print(f"  Tokens: {tokens}")
        print(f"  Count : {len(tokens)}\n")
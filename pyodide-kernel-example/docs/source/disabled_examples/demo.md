---
orphan: true
---

# Disabled examples

This page is intended to show how to disable the automatic insertion of the `TryExamples` button in the documentation. This is useful for methods that are not intended to be executed interactively or for those that may not work well in a notebook environment.

This page is listed in the [`try_examples.json`](../try_examples.json) file, and thus any examples on this page below -will not have the `TryExamples` button displayed.


## Example module

```{eval-rst}
.. dropdown:: Source code for ``disabled_example.py``
    :icon: code
    :color: info
    :animate: fade-in

    .. literalinclude:: disabled_example.py

```

## Rendered documentation

```{eval-rst}
.. automodule:: disabled_example
   :members:
```


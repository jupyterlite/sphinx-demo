---
orphan: true
---

# Disabled examples

This page is intended to show how to disable the automatic insertion of the `TryExamples` button in the documentation on a per-page basis. This is useful for methods that are not intended to be executed interactively or for those that may not work well in a WASM environment.

This page is ignored via a regex pattern in the [`try_examples.json`](../try_examples.json) file, like this:

```json
{
  "global_min_height": "400px",
  "ignore_patterns": ["disabled_examples\/demo.html"]
}
```

and thus any examples on this page below will not have the `TryExamples` buttons displayed.


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


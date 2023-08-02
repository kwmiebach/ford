# Ford

Ford is an experimental drop-in replacement for older versions of Prefect (up to version 2.4).

Designed to aid in a smooth transition when you decide to remove Prefect from a project, Ford is currently in the proof-of-concept stage.

## Usage example

Replace this:

```
import prefect as pf
from prefect import get_run_logger as pflog
```

With this:

```
import ford as pf
from ford import get_run_logger as pflog
```



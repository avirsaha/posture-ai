# MIT License
# Copyright (c) 2023 The_BDMI_Students_Exhibition_Team_2023
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
"""# View Library for MVC Design Pattern

This library contains `view` component in the MVC (Model-View-Controller) design pattern implemented in the project.

### Note: 
It is recommended that only specific functions, classes and objects are accesed.

## Compotents
```
import view.gui # Main GUI module.
import view.gui_util # GUI supporting functions.
```
## Metadata
- `Author:` Aviraj Saha
- `Date:` 2023-10-08 (YYYY-MM-DD)
- `Purpose:` View libraries contaning modules responsible for the presentation layer of the project."""

from . import gui, gui_util
__version__: str = "0.1.0-beta"
__all__: list[str] = ["gui", "gui_util"]
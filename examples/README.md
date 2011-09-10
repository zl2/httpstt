Examples
========

This directory contains some sample usage of httpstt.

audiomenu
---------

This is a simple audio menu. Take spoken commands and returns information in audio format.

### Installation

1. Replace the original `parseoutput.py` with this one.

2. Copy `city` to the same directory as `parseoutput.py`.

3. (Optional for weather information) Determine the city code for your city from www.theweathernetwork.com and replace the content of `city` with this code (the default is set to `usmo0830` corresponding to the city Peculiar.

### Testing

It is possible to test the weather RSS feed parser separately.

    python getrss.py

### Implementation notes

This example is distributed with an unmodified version of feedparser.py and html unescape function (see the corresponding files for their respective copyright and licenses).

It does not use `tts.py` and instead makes system calls of its own.
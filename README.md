Voice recognition and Text-to-speech (TTS) for http based servers
=================================================================

Quick start
-----------

All dependencies need to be installed beforehand.

### TTS Example

Put all files in the same place, say 

    /var/www/httpstt

Open

    www.yourdomain.com/httpstt/tts.py?text=hello

with a webbrowser. The webpage should contain a link to a wav
file. Play this file (it should be a voice saying "hello").

### STT Example

Put all files in the same place

    /var/www/httpstt

Change the 5 lines in

    /var/www/httpstt/convertone

to point to your installation of Sphinx and language model files.

Create a subdirectory data

    mkdir /var/www/httpstt/data

and allow write access to it

    chmod o+w /var/www/httpstt/data

(probably dangerous in general)
Open

    www.yourdomain.com/httpstt/stt.html

with a webbrowser and upload a wav file.

After uploaded, you should receive a webpage containg the text of the uploaded wav file.

Installation
------------

### Dependencies

All versions numbers are the test machine's version numbers. It may
work with other versions.

For voice recognition/speech-to-text (STT):

* python (2.5.2)
* sphinxbase (0.6)
* pocketsphinx (0.6)
* sox (14.0.0) [with support for the sndfile format]
* sh (or a compatible shell (e.g., bash) or it is possible to modify convertone to adapt to your shell/system)
* a webserver that runs python scripts (e.g., apache2 with mod_python)
* a better acoustic model (optional, the one available on voxforge seems to be quite good for English)

For TTS:

* espeak
* additional voices for espeak (optional)
* lame (3.97)

### List of Ubuntu packages

    sox sox-fmt-all lame

Depending on your version of Ubuntu, sphinxbase and pocketsphinx may
have to be compiled from source. If you choose not to run `sudo make
install`, it may be necessary to add `export LD_LIBRARY_PATH=...` at the
beginning of convertone.

### Others

You will also need a language model. A sample language model is
provided. Extract the archive `others/TAR3221.tgz` somewhere. Then
change the first few lines of convertone to point to the lm and dic
file. The available commands are:

			weather forecast
			radio station
			current time
			fortune cookie

Language models are also provided with the pocketsphinx package. Note
that `.lm` is not a standard file extension for language models (so the
lmfile should then be something like `turtle.DMP`).

Usage
-----

### Directory structure

All files are stored in data directory and your server need to be able
to write to this directory when files are uploaded.

### Testing

Test STT using stt.html by uploading a wav file. stt.py can be called
directly with a http POST request. If all went well, a link to the tts
answer should be returned from the POST request.

Test TTS using a http GET request to `tts.py?text=<text>` where `<text>`
is the text to be turned into sound.

It is also possible to test without an http server using the convert script.

Known issues
------------

System calls are made and a shell script is used (so this would probably not
work on a non-*nix computers without emulation)

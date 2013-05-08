RaspberryPi-Regattasegeln
=========================

Dabei geht es um die Vorbereitung eines Schülerinnen / Schülerwettbewerbs zu einer Modellsegelbootregatta auf dem Wasserband des Petrisbergs. Die Segelboote sollen automatisch durch den RaspberryPi gesteuert werden.

In dem Seminar sollen Konzepte, Modelle, Lösungen für die Boote und ihre Steuerung entwickelt und beispielhaft umgesetzt werden. Ziel ist es am Ende des Seminars zumindest ein Konzept für den Bau eines Bootes zu erarbeiten, welches autonom von A nach B segelt und dabei Hindernisse und andere Boote erkennt

Anleitung Kompilieren (C in Python benutzen)
============================================

```ruby
gcc -Wall -fPIC -c flags.c
gcc -shared -Wl,-soname,libflags.so.1 -o libflags.so flags.o

Python: from ctypes import *
mylib = CDLL("./liprpi_cmps10.so")
```

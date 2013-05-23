Anleitung zum Erstellen einer Library für Python:

c-Datei kompilieren:
gcc -o rpi_srf08 rpi_srf08.c
./rpi_srf08  // Kompilierte Datei wird ausgeführt

Shared Library erstellen:
gcc -Wall -fPIC -c rpi_srf08.c
gcc -shared -Wl,-soname,libflags.so.1 -o libflags.so rpi_srf08.o


Die Datei libflags.so kann jetzt in Python genutzt werden. Siehe test.py
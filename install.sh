#!/bin/sh
apt install python3-pip
pip3 install librosa dtw pyttsx pyaudio
apt install python3-tk

# Speak engine for say something and normalize audios (festival)
sudo apt-get install festival libasound-dev portaudio19-dev libportaudio2 libportaudiocpp0 libav-tools -y
wget https://github.com/guadalinex-archive/hispavoces/raw/master/packages/festvox-sflpc16k_1.0-1_all.deb
# Configure spanish dictionary on festival (more voices on https://github.com/guadalinex-archive/hispavoces)
sudo dpkg -i festvox-sflpc16k_1.0-1_all.deb && rm festvox-sflpc16k_1.0-1_all.deb
sudo cp voices.scm.festival /usr/share/festival/voices.scm

# Also you can use espeak https://ubuntuperonista.blogspot.com/2013/10/como-hago-text-to-speech-en-ubuntu.html

# Hide record library (espeak mrola) errors
export MALLOC_CHECK_=2

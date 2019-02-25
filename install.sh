#!/bin/sh
apt install python3-pip
pip3 install librosa dtw pyttsx
apt install python3-tk
# Speak engine for say something and normalize audios (festival)
apt-get install festival
wget https://github.com/guadalinex-archive/hispavoces/raw/master/packages/festvox-sflpc16k_1.0-1_all.deb
# Configure spanish dictionary on festival (more voices on https://github.com/guadalinex-archive/hispavoces)
sudo dpkg -i festvox-sflpc16k_1.0-1_all.deb && rm festvox-sflpc16k_1.0-1_all.deb
sudo cp voices.scm.festival /usr/share/festival/voices.scm

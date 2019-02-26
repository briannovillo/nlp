espeak -v mb-es1 $1 --stdout > ./normalized/$1.wav && espeak -v mb-es2 $1 --stdout > ./normalized2/$1.wav && espeak -v mb-vz1 $1 --stdout > ./normalized3/$1.wav && espeak -v mb-mx2 $1 --stdout > ./normalized4/$1.wav
echo $1 | text2wave -o ./normalized5/$1.wav

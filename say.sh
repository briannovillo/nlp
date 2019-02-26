espeak -v mb-es1 $1 --stdout > ./normalized/$1.wav
echo $1 | text2wave -o ./normalized2/$1.wav

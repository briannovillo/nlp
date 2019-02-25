#espeak $1 --stdout > ./normalized/$1.wav
echo $1 | text2wave -o ./normalized/$1.wav

N=50000
dt=0.001
A=5
B=3
CAP=$1
l=0.01


g++ func.cpp -std=c++17 -pthread -o func

python3 init.py $N $dt $A $B > tmp.txt
./func $N $l $CAP < tmp.txt > res.txt
python3 calc_corel.py $N $l $CAP < res.txt

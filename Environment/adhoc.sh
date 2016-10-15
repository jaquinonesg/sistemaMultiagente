sudo modprobe batman-adv
sudo ifconfig wlp3s0 down
sudo iwconfig wlp3s0 mode ad-hoc
sudo ifconfig wlp3s0 mtu 1532
sudo iwconfig wlp3s0 mode ad-hoc essid TLON-ADHOC ap 02:1B:55:AD:0C:02 channel 1
sudo sleep 2
sudo ip link set wlp3s0 up
sudo sleep 1
sudo batctl if add wlp3s0
sudo ifconfig bat0 10.0.0.5 netmask 255.255.255.0 up


import RPi.GPIO as gpio
import time, subprocess, os

def init():
	"""
	set pins output
	"""
	gpio.setmode(gpio.BCM)
	gpio.setup(2,gpio.IN)
	gpio.setup(3,gpio.IN)
	gpio.setup(4,gpio.OUT)
	gpio.setup(14,gpio.OUT)
	gpio.setup(15,gpio.OUT)
	gpio.setup(17,gpio.OUT)
	gpio.setup(18,gpio.OUT)
	animation(0.1)
	for i in range(3):
		animation(0)
		time.sleep(0.1)


def animation(duration):
	gpio.output(4,1)
	time.sleep(duration)
	gpio.output(14,1)
	time.sleep(duration)
	gpio.output(15,1)
	time.sleep(duration)
	gpio.output(17,1)
	time.sleep(duration)
	gpio.output(18,1)
	time.sleep(duration)

	if duration==0:
		time.sleep(0.1)

	gpio.output(4,0)
	time.sleep(duration)
	gpio.output(14,0)
	time.sleep(duration)
	gpio.output(15,0)
	time.sleep(duration)
	gpio.output(17,0)
	time.sleep(duration)
	gpio.output(18,0)
	time.sleep(duration)

def check():
	led_to_turn_on=[]
	if subprocess.check_output("host balrog.lan", shell=True)!=b'balrog.lan has address 172.23.42.254\n':
		#test for DNS
		led_to_turn_on.append(4)
		animation(0.01)
		#We can add DHCP if the dns crashes because it's the same program
		led_to_turn_on.append(15)

	if os.system("ping 172.23.42.254 -c 1 -A")!=0 and os.system("ping 172.23.42.201")!=0:
		#test if lan is up
		led_to_turn_on.append(14)
		animation(0.01)

	if subprocess.check_output("iwlist wlan0 scan | grep UrLab", shell=True)!=b'                    ESSID:"UrLab"\n':
		#test if UrLab SSID is available
		led_to_turn_on.append(17)
		animation(0.01)

	if os.system("ping 172.23.218.248 -c 1 -A")!=0 and os.system("ping 1.1.1.1 -c 1 -A")!=0:
		#test if internet&tinc are available
		led_to_turn_on.append(18)
		animation(0.01)
	"""
	DHCP check need to be written (not in a hurry as long as we are using dnsmasq)
	"""
	for i in range(3):
		time.sleep(0.1)
		animation(0)
	for i in range(len(led_to_turn_on)):
		gpio.output(led_to_turn_on[i],1)

	while True:
		if gpio.input(3)==0:
			break

def main():
	init()
	while True:
		if gpio.input(2) == 0:
			check()
		animation(0.1)


if __name__ == '__main__':
    main()
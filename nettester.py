#!/usr/bin/python3
import RPi.GPIO as gpio
import time
import subprocess
import os


def init(gpiout):
	"""
	set pins output
	"""
	gpio.setmode(gpio.BCM)
	gpio.setup(2, gpio.IN)
	gpio.setup(3, gpio.IN)
	for i in gpiout:
		gpio.setup(i, gpio.OUT)
	animation(0.1, gpiout)
	for i in range(3):
		animation(0, gpiout)


def animation(duration, gpiout):
	"""
	This is the animation function. It takes the delay between each LED
	and the list of GPIO output pins
	"""
	if duration != 0:
		for i in range(1, -1, -1):
			for j in gpiout:
				gpio.output(j, i)
				time.sleep(duration)
	else:
		for i in range(1, -1, -1):
			for j in gpiout:
				gpio.output(j, i)
			time.sleep(0.1)


def check(gpiout):
	"""
	this functions simply runs the tests and tells the system wich LED
	to turn on.
	"""
	led_to_turn_on = []

	if os.system("nslookup delight.lan | grep 172.23.42.201") != 0:
		# test for DNS
		led_to_turn_on.append(4)
		# We can add DHCP if the dns crashes because it's the same program
		led_to_turn_on.append(15)

	if os.system("ping 172.23.42.254 -c 1 -A") != 0 and os.system("ping 172.23.42.201 -c 1 -A") != 0:
		# test if lan is up
		led_to_turn_on.append(14)

	if subprocess.check_output("iwlist wlan0 scan | grep UrLab", shell=True) != b'                    ESSID:"UrLab"\n':
		# test if UrLab SSID is available
		led_to_turn_on.append(17)

	if os.system("ping 172.23.218.248 -c 1 -A") != 0 and os.system("ping 1.1.1.1 -c 1 -A") != 0:
		# test if internet&tinc are available
		led_to_turn_on.append(18)
	"""
	DHCP check need to be written (not in a hurry as long as we are using dnsmasq)
	"""


	for i in range(3):
		animation(0, gpiout)
	for i in led_to_turn_on:
		gpio.output(led_to_turn_on, 1)

	while True:
		if gpio.input(3) == 0:
			break


def main():
	gpiout = (4, 14, 15, 17, 18)
	init(gpiout)
	while True:
		if gpio.input(2) == 0:
			check(gpiout)
		animation(0.1, gpiout)


if __name__ == '__main__':
	main()

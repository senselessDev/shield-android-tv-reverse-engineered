reformat: boot.txt
	tr -d '\n' < boot.txt > .boot.txt
	sed -e 's/\[0D\]\[0A\]/\
	/g' .boot.txt > boot_cleaned.txt

threshold_applied.csv: boot.npy
	python threshold.py

boot.txt: threshold_applied.csv
	sigrok-cli -I csv:samplerate=2000000 -i threshold_applied.csv -P uart:baudrate=115200 -A uart=rx-data > boot.txt

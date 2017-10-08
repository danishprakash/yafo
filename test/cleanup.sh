#!/bin/sh

echo "this is the working directory $PWD"
echo "CAUTION: this script will force delete the directories in the current working directory"
echo
echo "Do you want to continue?: (1/0)"
read CONFIRM

if [ "$CONFIRM" == "1" ]; then
	rm -rf ./Documents
	rm -rf ./Images
	rm -rf ./Movies
	rm -rf ./Music
	rm -rf ./Programs
	rm -rf ./Scripts
	rm -rf ./Compressed
	rm -rf ./Rest
	echo "Current directory cleaned up."
else
	echo "Aborted"
fi


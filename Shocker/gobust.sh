#!/bin/bash

for i in $(ls -1 | grep small)
do
	gobuster -x php,html,sh dir -u http://10.10.10.56/cgi-bin -w $i
done

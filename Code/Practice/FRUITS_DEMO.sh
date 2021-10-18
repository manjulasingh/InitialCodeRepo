#!ksh/bin/bash

Input="FRUITS.txt"

rm -rf new_fruits.txt
rm -rf new_Fruits2.txt

while read line
do
	echo "$line" | sed 's/ //g' >> new_fruits.txt
	
done < $Input

cat new_Fruits.txt | sed 's/$/ /g' >> new_Fruits2.txt

cat new_Fruits2.txt | tr '\n' ' ' > new_Fruits3.txt

	
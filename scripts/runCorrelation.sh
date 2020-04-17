for file in /research/jagondzinski/resilience_output/thomp276/2020-04-17-csvOutput/*.csv
do
	if [ $# == 2 ]
	then
		echo python correlation.py "$file" "$1" "$2"
		python3 correlation.py "$file" "$1" "$2"
	else 
		echo python correlation.py "$file"
		python3 correlation.py "$file"
	fi
done

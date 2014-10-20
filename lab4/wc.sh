#!/bin/bash

# awk '

# /^CMSC/ { print c; c=$0 } !/^CMSC/ { c=c", "$0}
# END { print c}

# ' cmsc.txt  
# | awk '/[0-9]{4}, [0-9]{4}/ { print $7}
  # '

# awk '
 
# /^{{[0-9]{3}/ { a=$0; }
# /^[0-9]{4}/ { b=a", "$0; }
# /^[a-zA-Z:\.]+ [a-zA-Z\-]+/ { c=b", "$0; }
# /^Seats/ { d=c", "$3" "$5" "$7; }
# /^[MTuWThF]+ [0-9]+:/ { e=d", "$1", "$2" "$3" "$4; }
# /^[A-Z]{3} / { f=e", "$1", "$2; print f} 

# ' cmsc.txt | sed 's/)//g'

tail +2 worldcup.txt | sed 's/|align=center|{{sort dash}}/|0/g; 
s/style="background:#fff68f"|//g; s/FIFA World Cup|[0-9]\{4\}//g
 s/|style=white-space:nowrap|//g; s/|.*||.*||.*//g; 
 s/(//g; s/)//g; s/|//g; s/\[\[//g; s/\]\]//g; s/#1\*//g; 
 s/,//g; s/#2\^//g; s/<sup>#3#<\/sup>//g; s/{{fb//g; s/}//g; 
 s/-//g; /^$/d' | awk '
 {if ($0 ~ /[A-Z]{3}/) country=$0; } {if ($0 ~ /[A-Z]{3}/) pos=1; } 
 {if ($0 !~ /[A-Z]{3}/) print country", "$2", "pos"\n"country", "$3", "pos"\n"country", "$4", "pos"\n"country", "$5", "pos"\n"country", "$6", "pos"\n"country", "$7","pos++}' | sed '/^[A-Z]\{3\}, ,/d'
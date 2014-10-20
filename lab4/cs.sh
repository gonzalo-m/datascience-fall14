#!/bin/bash

# awk '

# /^CMSC/ { print c; c=$0 } !/^CMSC/ { c=c", "$0}
# END { print c}

# ' cmsc.txt  
# | awk '/[0-9]{4}, [0-9]{4}/ { print $7}
  # '

awk '
 
/^CMSC[0-9]{3}/ { a=$0; }
/^[0-9]{4}/ { b=a", "$0; }
/^[a-zA-Z:\.]+ [a-zA-Z\-]+/ { c=b", "$0; }
/^Seats/ { d=c", "$3" "$5" "$7; }
/^[MTuWThF]+ [0-9]+:/ { e=d", "$1", "$2" "$3" "$4; }
/^[A-Z]{3} / { f=e", "$1", "$2; print f}

' cmsc.txt | sed 's/)//g'

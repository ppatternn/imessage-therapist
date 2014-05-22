if [ $# -lt 1 ]; then
    echo "you gotta pass in a phone number as param e.g. +4356491672"
fi
login=$1

sqlite3 ~/Library/Messages/chat.db " 
select text from message, handle
where message.handle_id = handle.ROWID
and handle.id = '$1' " > "$1_messages.txt"

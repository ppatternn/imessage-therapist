import sys
import os
import sqlite3 as lite
#from nltk.corpus import stopwords
from textblob import TextBlob, Word


def copy_db():
    os.system("cp ~/Library/Messages/chat.db .")

def fetch_data(cmd):
    con = None
    try:
        db = 'chat.db'
        con = lite.connect(db)
        cur = con.cursor()
        cur.execute(cmd)
        data = cur.fetchall()
        return data
    except lite.Error, e:
        print "Error %s:" % e.args[0]
        sys.exit(1)
    finally:
        if con:
            con.close()

if __name__ == '__main__':
    copy_db()
    if len(sys.argv) > 1:
        number = sys.argv[1]
    else:
        print "needs phone number as argument, e.g. '+14356401672'"
        sys.exit()
    cmd = ('select chat.chat_identifier, text, is_from_me '
           'from message, handle, chat, chat_handle_join '
           'where chat.ROWID = chat_handle_join.chat_id '
           'and handle.ROWID = chat_handle_join.handle_id '
           'and message.handle_id = handle.ROWID '
           'and is_from_me = 0 '
           'and chat.room_name is null '
           'and handle.id = "%s" ' % number)
    data = fetch_data(cmd)
    tokens = [x[1] for x in data]
    joined = ' '.join(tokens)
    blob = TextBlob(joined)

    print "# messages recieved from %s" % number
    print len(data)
    print "%s's sentiment in texts w/ you: " % number
    print blob.sentiment

    cmd = ('select chat.chat_identifier, text, is_from_me '
           'from message, handle, chat, chat_handle_join '
           'where chat.ROWID = chat_handle_join.chat_id '
           'and handle.ROWID = chat_handle_join.handle_id '
           'and message.handle_id = handle.ROWID '
           'and is_from_me = 1 '
           'and chat.room_name is null '
           'and handle.id = "%s" ' % number)

    data = fetch_data(cmd)
    tokens = [x[1] for x in data]
    joined = ' '.join(tokens)
    blob = TextBlob(joined)

    print "# messages you've sent to %s" % number
    print len(data)
    print "your sentiment in texts w/ %s: " % number
    print blob.sentiment

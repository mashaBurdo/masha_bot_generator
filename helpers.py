import sqlite3

def word_combination():
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM words WHERE genere='adj' ORDER BY RANDOM() LIMIT 1")
    adj = cursor.fetchall()
    #print(adj)
    conn.close()

    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM words WHERE genere !='adj' ORDER BY RANDOM() LIMIT 1")
    word = cursor.fetchall()
    #print(word)
    conn.close()

    noEnd = adj[0][1][:len(adj[0][1])-2]

    if word[0][2] == 'he':
        result = adj[0][1] +" "+ word[0][1]
    elif word[0][2] == 'she':
        result = noEnd +"ая "+ word[0][1]
    elif word[0][2] == 'it':
        result = noEnd +"ое "+ word[0][1]

    return result

def holland_combination():
    conn = sqlite3.connect('words.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM words WHERE genere !='adj' ORDER BY RANDOM() LIMIT 1")
    word = cursor.fetchall()
    #print(word)
    conn.close()

    noEnd = 'голландск'

    if word[0][2] == 'he':
        result = noEnd +"ий "+ word[0][1]
    elif word[0][2] == 'she':
        result = noEnd +"ая "+ word[0][1]
    elif word[0][2] == 'it':
        result = noEnd +"ое "+ word[0][1]

    return result

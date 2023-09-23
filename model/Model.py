import csv
from model.Note import *

FILE_PATH = notes.csv

def save (new_note) :
    note_id = generate_id()
    
    with open(FILE_PATH, 'a', newline='') as csvnote:
        parameters = ['id', 'title', 'body', 'date']
        writer = csv.DictWriter(csvnote, parameters = parameters)
        
        if csvnote.tell() == 0:
            writer.writeheader() 
            
            new_note.id, new_note.date = note_id, dete.current()
            writer.writerow({'id' : new_note.id, 'title' : new_note.title, 'body' : new_note.body, 'date' : new_note.date})
            
def  generate_id () :
    try :
        with open(FILE_PATH, 'r', encoding='utf-8') as csvnote :
            reader = csv.DictReader(csvnote)
            current_id = max(int(row['id']) for row in reader)
        return current_id + 1
    except Exception as e :
        print(f"Input error : {e}")
        
def read (note_id) :
    try :
        with open(FILE_PATH, 'r', encoding='utf-8') as csvnote :
            reader = csv.DictReader(csvnote)
            for row in reader :
                if row ['id'] == note_id :
                    return Note(row['id'], row['title'], row['body'], row['date'])
        return None
    except Exception as e :
        print(f"Input error : {e}")
      
def edit (note_id, new_note) :
    notes = []
    
    with open (FILE_PATH, 'r', encoding='utf-8') as csvnote :
        reader = csv.DictReader(csvnote)
        for row in reader :
            edit_id = row['id']
            if edit_id == note_id :
                row['title'], row['body'], row['date'] = new_note.title, new_note.body, date.today()
    with open(FILE_PATH, 'w', newline='', encoding='utf-8') as csvnote :
        parameters = ['id', 'title', 'body', 'date']
        writer = csv.DictWriter(csvnote, parameters = parameters)
        writer.writeheader() 
        writer.writerows(notes)
        
def delete (note_id) :
    try :
        with open (FILE_PATH, 'r', encoding='utf-8') as csvnote :
            reader = csv.DictReader(csvnote)
            notes = [row for row in reader if row['id'] != note_id]
        
        with open(FILE_PATH, 'w', newline='', encoding='utf-8') as csvnote :
            parameters = ['id', 'title', 'body', 'date']
            writer = csv.DictWriter(csvnote, parameters = parameters)
            writer.writeheader() 
            writer.writerows(notes)
    except Exception as e :
        print(f"Input error : {e}")

def find_id (id = None) :
    try :
        notes = []
        with open(FILE_PATH, 'r', encoding='utf-8') as csvnote :
            reader = csv.DictReader(csvnote)
            for row in reader:
                note_id = row['id']
                if id is None or note_id == id :
                    notes.append (Note(note_id, row['title'], row['body'], row['date']))
        return notes
    except Exception as e :
        print(f"Input error : {e}")
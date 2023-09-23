from view.Menu import *
from model.Note import *

def menu() -> int:
    print(main_menu)
    while True:
        selection = input(menu_selection)
        if selection.isdigit() and 0 < int(selection) < 6:
            return int(selection)
        print(error_msg)
        
def new_entry (msg = None) :
    if msg != None :
        print_msg ("Please enter your note : " +  msg)
        title = input("Note title : ")
        body = input()
        note = Note(title, body)
        return note
    
def print_msg (msg : str):
    print (msg)

    
def find_by_id (msg = None):
    print_msg ("Enter note id : " + msg)
    id = input("ID: ")
    return id

def print_note (msg : str):
    if msg == None:
        print("No such note")
    else: 
        print(msg)
        
def print_all (notes : Note):
    print_msg("Your notes : ")
    if notes == None or notes == []:
        print("Empty")
    else:
        for note in notes:
            print_note(note)
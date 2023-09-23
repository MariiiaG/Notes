from model import Model
from view import View

def start() :
    while True : 
        option = View.menu()
        match option :
            case 1 :
                Model.save(View.new_entry("Create a new entry"))
            case 2 :
                View.print_all(Model.find_id())
                id = View.find_by_id("Edit a note")
                View.print_note(Model.read(id))
                Model.edit(id, View.new_entry())
            case 3 :
                View.print_all(Model.find_id())
                View.print_note(Model.read(View.find_by_id("Find a note")))
            case 4 :
                View.print_all(Model.find_id())
                id = View.find_by_id("Delete a note")
                View.print_note(Model.read(id))
                Model.delete(id)
            case 5 :
                break
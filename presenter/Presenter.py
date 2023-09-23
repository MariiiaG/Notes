from model import Model
from view import View

def start() :
    while True : 
        option = view.menu()
        match option :
            case 1 :
                Model.save(View.new_entry("Make a new note"))
            case 2 :
                View.print_all(Model)
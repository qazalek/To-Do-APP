import PySimpleGUI as Sg
import functions  # Assuming you have a module named 'functions' with required functions

input_box = Sg.InputText(tooltip="Enter todo", key="todo")
add_button = Sg.Button("Add")
list_box = Sg.Listbox(values=functions.get_todos(), key='todos',
                     enable_events=True, size=[45, 10])
edit_button = Sg.Button("Edit")

window = Sg.Window('My To-Do App',
                  layout=[[input_box, add_button], [list_box, edit_button]],
                  font=('Helvetica', 20))

while True:
    event, values = window.read()

    if event == Sg.WIN_CLOSED:
        break

    if event == "Add":
        todos = functions.get_todos()
        new_todo = values['todo'] + "\n"
        todos.append(new_todo)
        functions.write_todos(todos)

    if event == "Edit":
        todo_to_edit = values['todos'][0]  # Get the selected item from the listbox
        new_todo = values['todo'] + "\n"

        todos = functions.get_todos()
        index = todos.index(todo_to_edit)
        todos[index] = new_todo
        functions.write_todos(todos)

    window['todos'].update(values=functions.get_todos())

window.close()

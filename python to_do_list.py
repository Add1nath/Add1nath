
import android

def on_unlock(context):
    print("Hello!")

    to_do_list = ["Buy groceries", "Do laundry", "Call mom"]

    def show_to_do_list():
        print(to_do_list)

    def edit_to_do_list():
        print("Edit to-do list")

    button = android.Button(context)
    button.setOnClickListener(show_to_do_list)
    button.setOnLongClickListener(lambda view: print("Long click"))
    button.setX(0)
    button.setY(0)
    button.setText("To-Do List")
    button.show()

    edit_button = android.Button(context)
    edit_button.setOnClickListener(edit_to_do_list)
    edit_button.setX(-50)
    edit_button.setY(0)
    edit_button.setText("Edit")
    edit_button.show()

android.register_callback(android.EVENT_SCREEN_ON, on_unlock)

while True:
    android.sleep(1)

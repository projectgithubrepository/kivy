from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window

class MainApp(App):
    def build(self):
        self.operators = ["/", "*", "+", "-"]
        self.last_was_operator = None
        self.last_button = None
        main_layout = BoxLayout(orientation="vertical")
        self.solution = TextInput(
            multiline=False, readonly=True, halign="right", font_size=80
        )
        main_layout.add_widget(self.solution)
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            [".", "0", "C", "+"],
        ]
        for row in buttons:
            h_layout = BoxLayout()
            for label in row:
                button = Button(
                    text=label,
                    pos_hint={"center_x": 0.5, "center_y": 0.5},
                    font_size=50, background_color=[0.6, 1, 0.7, 1]
                )
                button.bind(on_press=self.on_button_press)
                h_layout.add_widget(button)
            main_layout.add_widget(h_layout)

        equals_button = Button(
            text="=", pos_hint={"center_x": 0.5, "center_y": 0.5}, font_size=80, background_color=[0, 1, 0.2, 1]
        )
        equals_button.bind(on_press=self.on_solution)
        main_layout.add_widget(equals_button)

        return main_layout

    def on_button_press(self, instance):
        current = self.solution.text
        button_text = instance.text

        if button_text == "C":
            # Clear the solution widget
            self.solution.text = ""
        else:
            if current and (
                self.last_was_operator and button_text in self.operators):
                # Don't add two operators right after each other
                return
            elif current == "" and button_text in self.operators:
                # First character cannot be an operator
                return
            else:
                new_text = current + button_text
                self.solution.text = new_text
        self.last_button = button_text
        self.last_was_operator = self.last_button in self.operators

    def on_solution(self, instance):
        text = self.solution.text
        if text:
            solution = str(eval(self.solution.text))
            self.solution.text = solution

    def on_stop(self):
    	Window.close()

if __name__ == "__main__":
    app = MainApp()
    app.run().close()


# Here’s how your calculator code works:
#     In lines 8 to 10, you create a list of operators and a couple of handy values, last_was_operator and last_button, that you’ll use later on.
#     In lines 11 to 15, you create a top-level layout main_layout and add a read-only TextInput widget to it.
#     In lines 16 to 21, you create a nested list of lists containing most of your buttons for the calculator.
#     In line 22, you start a for loop over those buttons. For each nested list you’ll do the following:
#         In line 23, you create a BoxLayout with a horizontal orientation.
#         In line 24, you start another for loop over the items in the nested list.
#         In lines 25 to 39, you create the buttons for the row, bind them to an event handler, and add the buttons to the horizontal BoxLayout from line 23.
#         In line 31, you add this layout to main_layout.
#     In lines 33 to 37, you create the equals button (=), bind it to an event handler, and add it to main_layout.
# Most of the widgets in your application will call .on_button_press(). Here’s how it works:

#     Line 41 takes the instance argument so you can access which widget called the function.

#     Lines 42 and 43 extract and store the value of the solution and the button text.

#     Lines 45 to 47 check to see which button was pressed. If the user pressed C, then you’ll clear the solution. Otherwise, move on to the else statement.

#     Line 49 checks if the solution has any pre-existing value.

#     Line 50 to 52 check if the last button pressed was an operator button. If it was, then solution won’t be updated. This is to prevent the user from having two operators in a row. For example, 1 */ is not a valid statement.

#     Lines 53 to 55 check to see if the first character is an operator. If it is, then solution won’t be updated, since the first value can’t be an operator value.

#     Lines 56 to 58 drop to the else clause. If none of the previous conditions are met, then update solution.

#     Line 59 sets last_button to the label of the last button pressed.

#     Line 60 sets last_was_operator to True or False depending on whether or not it was an operator character.

import random
import tkinter as tk
from tkinter import messagebox

class NumberGuessingGame:
      def __init__(self, root):
         self.root = root
         self.root.title("Number Guessing Game")
         self.root.geometry("350x250")
         self.root.resizable(False, False)

         self.number = random.randint(1, 100)
         self.attempts = 0

         # Title label
         self.title_label = tk.Label(
            root,
            text="🎯 Number Guessing Game",
            font=("Arial", 14, "bold")
         )
         self.title_label.pack(pady=10)

         # Info label
         self.info_label = tk.Label(
            root,
            text="Guess a number between 1 and 100"
         )
         self.info_label.pack()

         # Entry box
         self.guess_entry = tk.Entry(root, justify="center")
         self.guess_entry.pack(pady=10)

         # Guess button
         self.guess_button = tk.Button(
            root,
            text="Submit Guess",
            command=self.check_guess
         )
         self.guess_button.pack(pady=5)

         # Result label
         self.result_label = tk.Label(root, text="")
         self.result_label.pack(pady=5)

         # Restart button
         self.restart_button = tk.Button(
            root,
            text="Restart Game",
            command=self.restart_game
         )
         self.restart_button.pack(pady=10)

      def check_guess(self):
         try:
            guess = int(self.guess_entry.get())
            self.attempts += 1

            if guess < self.number:
               self.result_label.config(text="⬇ Too Low! Try again.")
            elif guess > self.number:
                  self.result_label.config(text="⬆ Too High! Try again.")
            else:
                  messagebox.showinfo("Congratulations!",        f"You guessed the number in {self.attempts} attempts!")
         except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number")

      def restart_game(self):
         self.number = random.randint(1, 100)
         self.attempts = 0
         self.guess_entry.delete(0, tk.END)
         self.result_label.config(text="New game started! Guess again.")


# Run the app
if __name__ == "__main__":
      root = tk.Tk()
      app = NumberGuessingGame(root)
      root.mainloop()

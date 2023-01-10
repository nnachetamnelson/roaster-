import tkinter as tk
import openpyxl

class RosterGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Roster Generator")

        self.staff = []

        # Create widgets
        self.name_label = tk.Label(self.root, text="Name:")
        self.name_entry = tk.Entry(self.root)
        self.add_button = tk.Button(self.root, text="Add", command=self.add_staff)
        self.generate_button = tk.Button(self.root, text="Generate roster", command=self.generate_roster)

        # Place widgets in a grid
        self.name_label.grid(row=0, column=0)
        self.name_entry.grid(row=0, column=1)
        self.add_button.grid(row=1, column=0)
        self.generate_button.grid(row=1, column=1)

    def add_staff(self):
        name = self.name_entry.get()
        self.staff.append({"name": name})

    def generate_roster(self):
        # Create an Excel workbook
        workbook = openpyxl.Workbook()
        worksheet = workbook.active

        # Add table headers
        worksheet["A1"] = "Name"
        worksheet["B1"] = "Day 1"
        worksheet["C1"] = "Day 2"
        worksheet["D1"] = "Day 3"
        worksheet["E1"] = "Day 4"
        worksheet["F1"] = "Day 5"
        worksheet["G1"] = "Day 6"
        worksheet["H1"] = "Day 7"

        # Add a row for each staff member
        row_num = 2
        for member in self.staff:
            worksheet[f"A{row_num}"] = member["name"]
            shift = "Day"
            for col_num in range(2, 8):
                worksheet[f"{openpyxl.utils.get_column_letter(col_num)}{row_num}"] = shift
                if shift == "Day":
                    shift = "Night"
                else:
                    shift = "Day"
            row_num += 1

        # Add a day off for the last staff member
        worksheet[f"H{row_num-1}"] = "Off"

        # Save the workbook
        workbook.save("roster.xlsx")

root = tk.Tk()
app = RosterGenerator(root)
root.mainloop()

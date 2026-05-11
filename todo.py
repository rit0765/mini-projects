import customtkinter as ctk

ctk.set_appearance_mode("Dark") # Режимы: "Light", "Dark", "System" (автоматический выбор в зависимости от ОС)
ctk.set_default_color_theme("blue") # Темы: "blue" (стандартная), "dark-blue", "green"

class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("To-Do.py")
        self.geometry("450x550")

        self.grid_columnconfigure(0, weight=1) # Элементы будут растягиваться по ширине
        self.grid_rowconfigure(1, weight=1)    # Список задач займет всё свободное место

        self.label = ctk.CTkLabel(self, text="Мои задачи", font=("Roboto Medium", 24))
        self.label.grid(row=0, column=0, pady=20, padx=20, sticky="ew")

        self.entry = ctk.CTkEntry(self, placeholder_text="Впишите новую задачу сюда...")
        self.entry.grid(row=2, column=0, pady=(10, 20), padx=20, sticky="ew")

        self.button_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.button_frame.grid(row=3, column=0, pady=(0, 20), padx=20, sticky="ew")
        self.button_frame.grid_columnconfigure((0, 1), weight=1)

        self.add_button = ctk.CTkButton(self.button_frame, text="Добавить", command=self.add_task, fg_color="green", hover_color="#006400")
        self.add_button.grid(row=0, column=0, padx=(0, 10), sticky="ew")

        self.delete_button = ctk.CTkButton(self.button_frame, text="Удалить", command=self.delete_task, fg_color="#CD5C5C", hover_color="#8B0000")
        self.delete_button.grid(row=0, column=1, padx=(10, 0), sticky="ew")
        
        self.tasks_frame = ctk.CTkScrollableFrame(self, label_text="Список дел")
        self.tasks_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")
        
        self.task_checkboxes = []

    def add_task(self):
        task_text = self.entry.get()
        if task_text:
            checkbox = ctk.CTkCheckBox(self.tasks_frame, text=task_text)
            checkbox.pack(pady=5, anchor="w", padx=10)
            self.task_checkboxes.append(checkbox)
            self.entry.delete(0, 'end') # Очистить поле ввода

    def delete_task(self):
        for checkbox in self.task_checkboxes[:]: 
            if checkbox.get() == 1:
                checkbox.destroy()
                self.task_checkboxes.remove(checkbox)

if __name__ == "__main__":
    app = App()
    app.mainloop()
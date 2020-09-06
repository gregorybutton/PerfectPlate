import tkinter as tk
import requests
from FoodItem import FoodItem
from tkinter.font import Font
from PIL import ImageTk


class PerfectPlate(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.parent = parent

        self.HEIGHT = 1000
        self.WIDTH = 800
        self.plate = []



        self.canvas = tk.Canvas(self.parent, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        # The title

        self.title_font = Font(family="Helvetica", size=55, weight="bold")
        self.project_title_label = tk.Label(self.parent, text="Perfect Plate", font=self.title_font, fg="#ff4d4d")
        self.project_title_label.place(relx=0.5, relwidth=.58, relheight=.07, anchor='n')

        # The plate image

        self.plate_image = ImageTk.PhotoImage(file='plate.png')
        self.plate_label = tk.Label(self.parent, image=self.plate_image)
        self.plate_label.place(relx=0.35, rely=0.08, relwidth=.3, relheight=.15)

        # The top section, green background, border = 5

        self.top_frame = tk.Frame(self.parent, bg='#9cc098', bd=5)
        self.top_frame.place(relx=0.5, rely=0.235, relwidth=0.5, relheight=0.045, anchor='n')
        self.food_entry = tk.Entry(self.top_frame, font=40, bd=3)
        self.food_entry.place(relwidth=.57, relheight=1)
        self.get_data_button = tk.Button(self.top_frame, text="Search", font=40, command=lambda: self.get_data(self.food_entry.get()))
        self.get_data_button.place(relx=0.6, rely=0.04, relheight=1, relwidth=0.4)

        # The Search result

        self.search_result_frame = tk.Frame(self.parent, bg='#9cc098')
        self.search_result_frame.place(relx=0.5, rely=0.29, relwidth=.98, relheight=0.1, anchor='n')
        self.search_result_font = Font(family="Book Antiqua", size=30, weight="bold")
        self.search_result_label = tk.Label(self.search_result_frame, text="Enter An Item",
                                            font=self.search_result_font, bg='#9cc098', fg="#e6e6e6")
        self.search_result_label.place(relwidth=.98, relheight=.6)

        # adding "Add To Plate" Button

        self.add_to_plate_btn = tk.Button(self.search_result_frame, text="Add To Plate",
                                          bg='#999999', font=40, command=lambda: self.add_to_plate())
        self.add_to_plate_btn.place(relx=0.415, rely=0.61, relheight=0.34, relwidth=0.15)
        self.add_to_plate_btn.place_forget()

        # Pictures: Carb, Protein, Fat, Section

        self.bottom_frame = tk.Frame(self.parent)
        self.bottom_frame.place(relx=0.5, rely=0.395, relwidth=.98, relheight=0.195, anchor='n')
        self.carbs_image = ImageTk.PhotoImage(file='carbs.png')
        self.carbs_image_label = tk.Label(self.bottom_frame, image=self.carbs_image)
        self.carbs_image_label.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.77)
        self.protein_image = ImageTk.PhotoImage(file='protein.png')
        self.protein_image_label = tk.Label(self.bottom_frame, image=self.protein_image)
        self.protein_image_label.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.77)
        self.fat_image = ImageTk.PhotoImage(file='fat.png')
        self.fat_image_label = tk.Label(self.bottom_frame, image=self.fat_image)
        self.fat_image_label.place(relx=0.7, rely=0, relwidth=0.2, relheight=0.77)

        # showing nutrient Values

        self.carbs_label = tk.Label(self.bottom_frame)
        self.carbs_label.place(relx=0.1, rely=0.79, relwidth=0.2, relheight=.14)
        self.carbs_label.place_forget()
        self.protein_label = tk.Label(self.bottom_frame)
        self.protein_label.place(relx=0.4, rely=0.79, relwidth=0.2, relheight=.14)
        self.protein_label.place_forget()
        self.fat_label = tk.Label(self.bottom_frame)
        self.fat_label.place(relx=0.7, rely=0.79, relwidth=0.2, relheight=.14)
        self.fat_label.place_forget()

        # The plate section

        self.plate_frame = tk.Frame(self.parent)  # Plate Frame
        self.plate_frame.place(relx=0.5, rely=0.58, relwidth=.98, relheight=0.4, anchor='n')
        self.plate_food_item_font = Font(family="Book Antiqua", size=30, weight="bold")
        self.item1_label = tk.Label(self.plate_frame, text="", font=self.plate_food_item_font, bg='#e2ebe0', fg="#0a100a")
        self.item1_label.place(relx=0.5, rely=0.0, relwidth=.98, relheight=.2, anchor='n')
        self.item2_label = tk.Label(self.plate_frame, text="", font=self.plate_food_item_font, bg='#e2ebe0', fg="#0a100a")
        self.item2_label.place(relx=0.5, rely=0.225, relwidth=.98, relheight=.2, anchor='n')
        self.item3_label = tk.Label(self.plate_frame, text="", font=self.plate_food_item_font, bg='#e2ebe0', fg="#0a100a")
        self.item3_label.place(relx=0.5, rely=0.450, relwidth=.98, relheight=.2, anchor='n')
        self.item4_label = tk.Label(self.plate_frame, text="", font=self.plate_food_item_font, bg='#f0f5ef', fg="#0a100a")
        self.item4_label.place(relx=0.5, rely=0.7, relwidth=.98, relheight=.25, anchor='n')

    def get_data(self, item):

        # https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=Cheddar%20Cheese              # From: https://fdc.nal.usda.gov/api-guide.html

        api_key = 'hmx2uvyGhXzqQQ8jl09Blje66SHZwgtTaL9MLeK1'
        params = {'api_key': api_key}
        data = {'generalSearchInput': item}
        response = requests.post(r'https://api.nal.usda.gov/fdc/v1/foods/search', params=params, json=data)
        result = response.json()

        item_description = result['foods'][0]['description']        # getting the description of the item searched

        # variables totalling carbs, proteins, and fats

        nutrient_carbs_total = 0            # variable to hold carbs
        nutrient_protein_total = 0          # variable to hold protein
        nutrient_fat_total = 0              # variable to hold fat

        for nutrient in result['foods'][0]['foodNutrients']:                # looking for carbs proteins and fats,
            nutrient_id = nutrient['nutrientId']                            # since I don't know how query a json file
            nutrient_value = nutrient['value']

            if nutrient_id == 1003:
                nutrient_protein_total = nutrient_value
            elif nutrient_id == 1004:
                nutrient_fat_total = nutrient_value
            elif nutrient_id == 1005:
                nutrient_carbs_total = nutrient_value



        fi = FoodItem(item_description, nutrient_carbs_total, nutrient_protein_total, nutrient_fat_total)

        carbs_text = str(fi.get_carbs) + " G"
        protein_text = str(fi.get_protein) + " G"
        fat_text = str(fi.get_fat) + " G"

        # showing nutrient Values

        nutrient_result_font = Font(family="Book Antiqua", size=20, weight="bold")
        self.carbs_label.config(text=carbs_text, font=nutrient_result_font, fg="#161f14")
        self.carbs_label.place(relx=0.1, rely=0.79, relwidth=0.2, relheight=.14)
        self.protein_label.config(text=protein_text, font=nutrient_result_font, fg="#161f14")
        self.protein_label.place(relx=0.4, rely=0.79, relwidth=0.2, relheight=.14)
        self.fat_label.config(text=fat_text, font=nutrient_result_font, fg="#161f14")
        self.fat_label.place(relx=0.7, rely=0.79, relwidth=0.2, relheight=.14)

        self.search_result_label.config(text=item_description, fg='#212f1e')

        self.add_to_plate_btn.place(relx=0.415, rely=0.61, relheight=0.34, relwidth=0.15)



    def add_to_plate(self):
        self.search_result_label.config(text="Enter An Item", fg="#e6e6e6")
        self.add_to_plate_btn.place_forget()
        self.food_entry.delete(0, 'end')

        self.carbs_label.place_forget()
        self.protein_label.place_forget()
        self.fat_label.place_forget()

        self.plate.add()



if __name__ == "__main__":
    root = tk.Tk()
    PP = PerfectPlate(root)
    root.mainloop()
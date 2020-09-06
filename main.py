from tkinter import Tk, Canvas, Label, Button, Frame, Entry
import requests
from FoodItem import FoodItem
from tkinter.font import Font
from PIL import ImageTk


class PerfectPlate(Frame):
    def __init__(self, parent=None):
        Frame.__init__(self, parent)
        self.parent = parent
        self.winfo_toplevel().title("Perfect Plate")

        self.HEIGHT = 1000
        self.WIDTH = 800
        self.plate = []
        self.tempItem = []


        self.canvas = Canvas(self.parent, height=self.HEIGHT, width=self.WIDTH)
        self.canvas.pack()

        # The title

        self.title_font = Font(family="Helvetica", size=55, weight="bold")
        self.project_title_label = Label(self.parent, text="Perfect Plate", font=self.title_font, fg="#ff4d4d")
        self.project_title_label.place(relx=0.5, relwidth=.58, relheight=.07, anchor='n')

        # The plate image

        self.plate_image = ImageTk.PhotoImage(file='plate.png')
        self.plate_label = Label(self.parent, image=self.plate_image)
        self.plate_label.place(relx=0.35, rely=0.08, relwidth=.3, relheight=.15)

        # The top section, green background, border = 5

        self.top_frame = Frame(self.parent, bg='#9cc098', bd=5)
        self.top_frame.place(relx=0.5, rely=0.235, relwidth=0.5, relheight=0.045, anchor='n')
        self.food_entry = Entry(self.top_frame, font=40, bd=3)
        self.food_entry.place(relwidth=.57, relheight=1)
        self.get_data_button = Button(self.top_frame, text="Search", font=40, command=lambda: self.get_data(self.food_entry.get()))
        self.get_data_button.place(relx=0.6, rely=0.04, relheight=1, relwidth=0.4)

        # Adding clear Plate button

        self.clear_plate_frame = Frame(self.parent, bg='#9cc098', bd=5)
        self.clear_plate_frame.place(relx=0.9, rely=0.235, relwidth=0.13, relheight=0.045, anchor='n')
        self.clear_plate_btn = Button(self.clear_plate_frame, text="Clear Plate", font=40, command=lambda: self.clear_plate())
        self.clear_plate_btn.place(relx=0.5, rely=0.0, relwidth=1, relheight=1, anchor='n')

        # The Search result

        self.search_result_frame = Frame(self.parent, bg='#9cc098')
        self.search_result_frame.place(relx=0.5, rely=0.29, relwidth=.98, relheight=0.1, anchor='n')
        self.search_result_font = Font(family="Book Antiqua", size=30, weight="bold")
        self.search_result_label = Label(self.search_result_frame, text="Enter An Item",
                                            font=self.search_result_font, bg='#9cc098', fg="#e6e6e6")
        self.search_result_label.place(relwidth=.98, relheight=.6)

        # adding "Add To Plate" Button

        self.add_to_plate_btn = Button(self.search_result_frame, text="Add To Plate",
                                          bg='#999999', font=40, command=lambda: self.add_to_plate())
        self.add_to_plate_btn.place(relx=0.415, rely=0.61, relheight=0.34, relwidth=0.15)
        self.add_to_plate_btn.place_forget()

        # Pictures: Carb, Protein, Fat, Section

        self.bottom_frame = Frame(self.parent)
        self.bottom_frame.place(relx=0.5, rely=0.395, relwidth=.98, relheight=0.195, anchor='n')
        self.carbs_image = ImageTk.PhotoImage(file='carbs.png')
        self.carbs_image_label = Label(self.bottom_frame, image=self.carbs_image)
        self.carbs_image_label.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.77)
        self.protein_image = ImageTk.PhotoImage(file='protein.png')
        self.protein_image_label = Label(self.bottom_frame, image=self.protein_image)
        self.protein_image_label.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.77)
        self.fat_image = ImageTk.PhotoImage(file='fat.png')
        self.fat_image_label = Label(self.bottom_frame, image=self.fat_image)
        self.fat_image_label.place(relx=0.7, rely=0, relwidth=0.2, relheight=0.77)

        # showing nutrient Values

        self.carbs_label = Label(self.bottom_frame)
        self.carbs_label.place(relx=0.1, rely=0.79, relwidth=0.2, relheight=.14)
        self.carbs_label.place_forget()
        self.protein_label = Label(self.bottom_frame)
        self.protein_label.place(relx=0.4, rely=0.79, relwidth=0.2, relheight=.14)
        self.protein_label.place_forget()
        self.fat_label = Label(self.bottom_frame)
        self.fat_label.place(relx=0.7, rely=0.79, relwidth=0.2, relheight=.14)
        self.fat_label.place_forget()

        # The plate section

        self.plate_frame = Frame(self.parent)
        self.plate_frame.place(relx=0.5, rely=0.58, relwidth=.98, relheight=0.4, anchor='n')

        self.plate_food_item_font = Font(family="Book Antiqua", size=25)
        self.plate_food_nutrition_font = Font(family="Book Antiqua italic", size=13)


        self.food1_frame = Frame(self.plate_frame, bg='#d3e2d0')
        self.food1_frame.place(relx=0.5, rely=0.0, relwidth=.8, relheight=.2, anchor='n')

        self.food1_description_label = Label(self.food1_frame, text="Big ol salami Sandwich", font=self.plate_food_item_font, bg='#d3e2d0', fg="#0a100a")
        self.food1_description_label.place(relx=1, rely=0.22, relwidth=1.0, relheight=.6, anchor='e')
        self.food1_description_label.place_forget()

        self.food1_nutrition_label = Label(self.food1_frame, text="52 Grams/22 Grams/19 Grams", font=self.plate_food_nutrition_font, bg='#d3e2d0', fg="#0a100a")
        self.food1_nutrition_label.place(relx=1, rely=0.78, relwidth=1.0, relheight=.5, anchor='e')
        self.food1_nutrition_label.place_forget()


        self.food2_frame = Frame(self.plate_frame, bg='#d3e2d0')
        self.food2_frame.place(relx=0.5, rely=0.225, relwidth=.8, relheight=.2, anchor='n')
        self.food2_description_label = Label(self.food2_frame, text="A thick Juicy Burger", font=self.plate_food_item_font, bg='#d3e2d0', fg="#0a100a")
        self.food2_description_label.place(relx=1, rely=0.22, relwidth=1.0, relheight=.6, anchor='e')
        self.food2_description_label.place_forget()
        self.food2_nutrition_label = Label(self.food2_frame, text="52 Grams/22 Grams/19 Grams", font=self.plate_food_nutrition_font, bg='#d3e2d0', fg="#0a100a")
        self.food2_nutrition_label.place(relx=1, rely=0.78, relwidth=1.0, relheight=.5, anchor='e')
        self.food2_nutrition_label.place_forget()

        self.food3_frame = Frame(self.plate_frame, bg='#d3e2d0')
        self.food3_frame.place(relx=0.5, rely=0.450, relwidth=.8, relheight=.2, anchor='n')
        self.food3_description_label = Label(self.food3_frame, text="Cheeseburger", font=self.plate_food_item_font, bg='#d3e2d0', fg="#0a100a")
        self.food3_description_label.place(relx=1, rely=0.22, relwidth=1.0, relheight=.6, anchor='e')
        self.food3_description_label.place_forget()
        self.food3_nutrition_label = Label(self.food3_frame, text="52 Grams/22 Grams/19 Grams", font=self.plate_food_nutrition_font, bg='#d3e2d0', fg="#0a100a")
        self.food3_nutrition_label.place(relx=1, rely=0.78, relwidth=1.0, relheight=.5, anchor='e')
        self.food3_nutrition_label.place_forget()


        # Instanciating Plate Total Labels

        self.plate_total_frame = Frame(self.plate_frame, bg='#e2ebe0')
        self.plate_total_frame.place(relx=0.5, rely=0.68, relwidth=.8, relheight=.3, anchor='n')

        self.plate_total_plate_font = Font(family="Book Antiqua italic", size=22, weight="bold")
        self.plate_total_description_label = Label(self.plate_total_frame, text="Plate", font=self.plate_total_plate_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_description_label.place(relx=0.5, rely=0.1, relwidth=.15, relheight=.3, anchor='n')
        self.plate_total_description_label.place_forget()

        self.plate_total_desc_font = Font(family="Book Antiqua", size=12, weight="bold")
        self.plate_total_font = Font(family="Book Antiqua", size=25, weight="bold")

        self.plate_total_carbs_desc_label = Label(self.plate_total_frame, text="Carb", font=self.plate_total_desc_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_carbs_desc_label.place(relx=0.1, rely=0.64, relwidth=.06, relheight=.2, anchor='n')
        self.plate_total_carbs_desc_label.place_forget()
        self.plate_total_carbs_totals_label = Label(self.plate_total_frame, text="100.35 G", font=self.plate_total_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_carbs_totals_label.place(relx=0.24, rely=0.555, relwidth=.2, relheight=.25, anchor='n')
        self.plate_total_carbs_totals_label.place_forget()

        self.plate_total_protein_desc_label = Label(self.plate_total_frame, text="Protein", font=self.plate_total_desc_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_protein_desc_label.place(relx=0.4, rely=0.64, relwidth=.09, relheight=.2, anchor='n')
        self.plate_total_protein_desc_label.place_forget()
        self.plate_total_protein_totals_label = Label(self.plate_total_frame, text="100.35 G", font=self.plate_total_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_protein_totals_label.place(relx=0.55, rely=0.555, relwidth=.2, relheight=.25, anchor='n')
        self.plate_total_protein_totals_label.place_forget()

        self.plate_total_fat_desc_label = Label(self.plate_total_frame, text="Fat", font=self.plate_total_desc_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_fat_desc_label.place(relx=0.685, rely=0.64, relwidth=.05, relheight=.2, anchor='n')
        self.plate_total_fat_desc_label.place_forget()
        self.plate_total_fat_totals_label = Label(self.plate_total_frame, text="100.35 G", font=self.plate_total_font, bg='#e2ebe0', fg="#0a100a")
        self.plate_total_fat_totals_label.place(relx=0.815, rely=0.555, relwidth=.2, relheight=.25, anchor='n')
        self.plate_total_fat_totals_label.place_forget()



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
        self.tempItem.append(fi)

        carbs_text = str(fi.get_carbs()) + " G"
        protein_text = str(fi.get_protein()) + " G"
        fat_text = str(fi.get_fat()) + " G"

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


    def clear_plate(self):
        self.add_to_plate_btn.place_forget()
        self.food_entry.delete(0, 'end')

        self.plate.clear()
        self.tempItem.clear()

        self.carbs_label.place_forget()
        self.protein_label.place_forget()
        self.fat_label.place_forget()

        self.food1_description_label.place_forget()
        self.food1_nutrition_label.place_forget()
        self.food2_description_label.place_forget()
        self.food2_nutrition_label.place_forget()
        self.food3_description_label.place_forget()
        self.food3_nutrition_label.place_forget()
        self.plate_total_description_label.place_forget()
        self.plate_total_carbs_desc_label.place_forget()
        self.plate_total_carbs_totals_label.place_forget()
        self.plate_total_protein_desc_label.place_forget()
        self.plate_total_protein_totals_label.place_forget()
        self.plate_total_fat_desc_label.place_forget()
        self.plate_total_fat_totals_label.place_forget()


    def add_to_plate(self):
        self.search_result_label.config(text="Enter An Item", fg="#e6e6e6")
        self.add_to_plate_btn.place_forget()
        self.food_entry.delete(0, 'end')

        self.carbs_label.place_forget()
        self.protein_label.place_forget()
        self.fat_label.place_forget()

        self.plate.append(self.tempItem[0])         #adding item to plate
        self.tempItem.clear()                       #clearing temp list

        count = len(self.plate)

        if count == 1:
            self.food1_description_label.config(text=self.plate[0].get_name())
            self.food1_description_label.place(relx=1, rely=0.22, relwidth=1.0, relheight=.6, anchor='e')
            text = str(self.plate[0].get_carbs()) + " Grams/" + str(self.plate[0].get_protein()) + " Grams/" + str(self.plate[0].get_fat()) + " Grams"
            self.food1_nutrition_label.config(text=text)
            self.food1_nutrition_label.place(relx=1, rely=0.78, relwidth=1.0, relheight=.5, anchor='e')
            self.update_plate_totals()
        elif count == 2:
            self.food2_description_label.config(text=self.plate[1].get_name())
            self.food2_description_label.place(relx=1, rely=0.22, relwidth=1.0, relheight=.6, anchor='e')
            text = str(self.plate[1].get_carbs()) + " Grams/" + str(self.plate[1].get_protein()) + " Grams/" + str(self.plate[1].get_fat()) + " Grams"
            self.food2_nutrition_label.config(text=text)
            self.food2_nutrition_label.place(relx=1, rely=0.78, relwidth=1.0, relheight=.5, anchor='e')
            self.update_plate_totals()
        elif count == 3:
            self.food3_description_label.config(text=self.plate[2].get_name())
            self.food3_description_label.place(relx=1, rely=0.22, relwidth=1.0, relheight=.6, anchor='e')
            text = str(self.plate[2].get_carbs()) + " Grams/" + str(self.plate[2].get_protein()) + " Grams/" + str(self.plate[2].get_fat()) + " Grams"
            self.food3_nutrition_label.config(text=text)
            self.food3_nutrition_label.place(relx=1, rely=0.78, relwidth=1.0, relheight=.5, anchor='e')
            self.update_plate_totals()

    def update_plate_totals(self):
        self.plate_total_description_label.place(relx=0.5, rely=0.1, relwidth=.15, relheight=.3, anchor='n')

        carbs_total = 0
        protein_total = 0
        fat_total = 0

        for foodItem in self.plate:
            carbs_total += foodItem.get_carbs()
            protein_total += foodItem.get_protein()
            fat_total += foodItem.get_fat()


        self.plate_total_carbs_desc_label.place(relx=0.1, rely=0.64, relwidth=.06, relheight=.2, anchor='n')
        self.plate_total_carbs_totals_label.config(text=carbs_total)
        self.plate_total_carbs_totals_label.place(relx=0.24, rely=0.555, relwidth=.2, relheight=.25, anchor='n')

        self.plate_total_protein_desc_label.place(relx=0.4, rely=0.64, relwidth=.09, relheight=.2, anchor='n')
        self.plate_total_protein_totals_label.config(text=protein_total)
        self.plate_total_protein_totals_label.place(relx=0.55, rely=0.555, relwidth=.2, relheight=.25, anchor='n')

        self.plate_total_fat_desc_label.place(relx=0.685, rely=0.64, relwidth=.05, relheight=.2, anchor='n')
        self.plate_total_fat_totals_label.config(text=fat_total)
        self.plate_total_fat_totals_label.place(relx=0.815, rely=0.555, relwidth=.2, relheight=.25, anchor='n')




root = Tk()
PP = PerfectPlate(root)
root.mainloop()

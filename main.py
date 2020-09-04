import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk
import requests

HEIGHT = 1000
WIDTH = 800






def get_data(item):

    # https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=Cheddar%20Cheese              # From: https://fdc.nal.usda.gov/api-guide.html

    API_KEY = 'hmx2uvyGhXzqQQ8jl09Blje66SHZwgtTaL9MLeK1'
    params = {'api_key': API_KEY}
    data = {'generalSearchInput': item}
    response = requests.post(r'https://api.nal.usda.gov/fdc/v1/foods/search', params=params, json=data)
    result = response.json()

    item_description = result['foods'][0]['description']        # getting the description of the item searched



    # global variables totalling carbs, proteins, and fats

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

    carbs_text = str(nutrient_carbs_total) + " G"
    protein_text = str(nutrient_protein_total) + " G"
    fat_text = str(nutrient_fat_total) + " G"

    # showing nutrient Values

    nutrient_result_font = Font(family="Book Antiqua", size=20, weight="bold")
    carbs_label.config(text=carbs_text, font=nutrient_result_font, fg="#161f14")
    carbs_label.place(relx=0.1, rely=0.79, relwidth=0.2, relheight=.14)
    protein_label.config(text=protein_text, font=nutrient_result_font, fg="#161f14")
    protein_label.place(relx=0.4, rely=0.79, relwidth=0.2, relheight=.14)
    fat_label.config(text=fat_text, font=nutrient_result_font, fg="#161f14")
    fat_label.place(relx=0.7, rely=0.79, relwidth=0.2, relheight=.14)

    search_result_label.config(text=item_description, fg='#212f1e')

    add_to_plate_btn.place(relx=0.415, rely=0.61, relheight=0.34, relwidth=0.15)



def add_to_plate():
    search_result_label.config(text="Enter An Item", fg="#e6e6e6")
    add_to_plate_btn.place_forget()
    food_entry.delete(0, 'end')

    carbs_label.place_forget()
    protein_label.place_forget()
    fat_label.place_forget()



root = tk.Tk()  # referring to the screen

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()



#

my_font = Font(family="Helvetica", size=55, weight="bold")
project_title_label = tk.Label(root, text="Perfect Plate", font=my_font, fg="#ff4d4d")
project_title_label.place(relx=0.5, relwidth=.58, relheight=.07, anchor='n')



#

plate_image = ImageTk.PhotoImage(file='plate.png')  # plate image
plate_label = tk.Label(root, image=plate_image)
plate_label.place(relx=0.35, rely=0.08, relwidth=.3, relheight=.15)



#

top_frame = tk.Frame(root, bg='#9cc098', bd=5)  # The top section, green background, border = 5
top_frame.place(relx=0.5, rely=0.235, relwidth=0.5, relheight=0.045, anchor='n')
food_entry = tk.Entry(top_frame, font=40, bd=3)  # text box
food_entry.place(relwidth=.57, relheight=1)
get_data_button = tk.Button(top_frame, text="Search", font=40, command=lambda: get_data(food_entry.get()))
get_data_button.place(relx=0.6, rely=0.04, relheight=1, relwidth=0.4)



# The Search result

search_result_frame = tk.Frame(root, bg='#9cc098')  # The bottom section,
search_result_frame.place(relx=0.5, rely=0.29, relwidth=.98, relheight=0.1, anchor='n')
search_result_font = Font(family="Book Antiqua", size=30, weight="bold")
search_result_label = tk.Label(search_result_frame, text="Enter An Item", font=search_result_font, bg='#9cc098', fg="#e6e6e6")
search_result_label.place(relwidth=.98, relheight=.6)

# adding "Add To Plate" Button

add_to_plate_btn = tk.Button(search_result_frame, text="Add To Plate", bg='#999999', font=40, command=lambda: add_to_plate())
add_to_plate_btn.place(relx=0.415, rely=0.61, relheight=0.34, relwidth=0.15)
add_to_plate_btn.place_forget()




# Pictures: Carb, Protein, Fat, Section

bottom_frame = tk.Frame(root)
bottom_frame.place(relx=0.5, rely=0.395, relwidth=.98, relheight=0.195, anchor='n')
carbs_image = ImageTk.PhotoImage(file='carbs.png')                                  # carbs image
carbs_image_label = tk.Label(bottom_frame, image=carbs_image)
carbs_image_label.place(relx=0.1, rely=0, relwidth=0.2, relheight=0.77)
protein_image = ImageTk.PhotoImage(file='protein.png')                              # protein image
protein_image_label = tk.Label(bottom_frame, image=protein_image)
protein_image_label.place(relx=0.4, rely=0, relwidth=0.2, relheight=0.77)
fat_image = ImageTk.PhotoImage(file='fat.png')                                      # fat image
fat_image_label = tk.Label(bottom_frame, image=fat_image)
fat_image_label.place(relx=0.7, rely=0, relwidth=0.2, relheight=0.77)



# showing nutrient Values

carbs_label = tk.Label(bottom_frame)
carbs_label.place(relx=0.1, rely=0.79, relwidth=0.2, relheight=.14)
carbs_label.place_forget()
protein_label = tk.Label(bottom_frame)
protein_label.place(relx=0.4, rely=0.79, relwidth=0.2, relheight=.14)
protein_label.place_forget()
fat_label = tk.Label(bottom_frame)
fat_label.place(relx=0.7, rely=0.79, relwidth=0.2, relheight=.14)
fat_label.place_forget()



# plate section

plate_frame = tk.Frame(root)  # Plate Frame
plate_frame.place(relx=0.5, rely=0.58, relwidth=.98, relheight=0.4, anchor='n')
plate_food_item_font = Font(family="Book Antiqua", size=30, weight="bold")
item1_label = tk.Label(plate_frame, text="", font=plate_food_item_font, bg='#e2ebe0', fg="#0a100a")
item1_label.place(relx=0.5, rely=0.0, relwidth=.98, relheight=.2, anchor='n')
item2_label = tk.Label(plate_frame, text="", font=plate_food_item_font, bg='#e2ebe0', fg="#0a100a")
item2_label.place(relx=0.5, rely=0.225, relwidth=.98, relheight=.2, anchor='n')
item3_label = tk.Label(plate_frame, text="", font=plate_food_item_font, bg='#e2ebe0', fg="#0a100a")
item3_label.place(relx=0.5, rely=0.450, relwidth=.98, relheight=.2, anchor='n')
item4_label = tk.Label(plate_frame, text="", font=plate_food_item_font, bg='#f0f5ef', fg="#0a100a")
item4_label.place(relx=0.5, rely=0.7, relwidth=.98, relheight=.25, anchor='n')






root.mainloop()
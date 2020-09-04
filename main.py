import tkinter as tk
from tkinter.font import Font
from PIL import ImageTk
import requests

HEIGHT = 950
WIDTH = 800



# def title():
#     my_font = Font(family="Helvetica", size=55, weight="bold")
#     label1 = tk.Label(root, text="Perfect Plate", font=my_font, fg="#ff4d4d")
#     label1.place(relx=0.5, relwidth=.9, relheight=.1, anchor='n')


# def plate_image():
#     plate_image = ImageTk.PhotoImage(file='plate.png')  # plate image
#     plate_label = tk.Label(root, image=plate_image)
#     plate_label.place(relx=0.35, rely=0.075, relwidth=.3, relheight=.2)



# def food_search():
#     top_frame = tk.Frame(root, bg='#9cc098', bd=5)  # The top section, green background, border = 5
#     top_frame.place(relx=0.5, rely=0.26, relwidth=0.5, relheight=0.045, anchor='n')
#
#     food_entry = tk.Entry(top_frame, font=40, bd=3)  # text box
#     food_entry.place(relwidth=.57, relheight=1)
#
#     button = tk.Button(top_frame, text="Search", font=40, command=lambda: get_data(food_entry.get()))
#     button.place(relx=0.6, rely=0.04, relheight=1, relwidth=0.4)


# def search_result_area():
#     search_result_frame = tk.Frame(root, bg='#9cc098')  # The bottom section,
#     search_result_frame.place(relx=0.5, rely=0.31, relwidth=.98, relheight=0.12, anchor='n')
#
#     search_result_font = Font(family="Helvetica", size=30, weight="bold")
#     item_label = tk.Label(search_result_frame, text="Enter An Item", font=search_result_font, bg='#9cc098',
#                           fg="#f2f2f2")
#     item_label.place(relwidth=.98, relheight=.45)




# def nutrient_images():
#     bottom_frame = tk.Frame(root)  # The bottom section,
#     bottom_frame.place(relx=0.5, rely=0.43, relwidth=.98, relheight=0.16, anchor='n')
#
#     carbs_image = ImageTk.PhotoImage(file='carbs.png')  # carbs image
#     carbs_image_label = tk.Label(bottom_frame, image=carbs_image)
#     carbs_image_label.place(relx=0.1, rely=0.0, relwidth=0.2, relheight=1)
#
#     protein_image = ImageTk.PhotoImage(file='protein.png')  # protein image
#     protein_image_label = tk.Label(bottom_frame, image=protein_image)
#     protein_image_label.place(relx=0.4, rely=0.0, relwidth=0.2, relheight=1)
#
#     fat_image = ImageTk.PhotoImage(file='fat.png')  # fat image
#     fat_label = tk.Label(bottom_frame, image=fat_image)
#     fat_label.place(relx=0.7, rely=0.0, relwidth=0.2, relheight=1)



def get_data(item):

    # https://api.nal.usda.gov/fdc/v1/foods/search?api_key=DEMO_KEY&query=Cheddar%20Cheese              # From: https://fdc.nal.usda.gov/api-guide.html

    API_KEY = 'hmx2uvyGhXzqQQ8jl09Blje66SHZwgtTaL9MLeK1'
    params = {'api_key': API_KEY}
    data = {'generalSearchInput': item}
    response = requests.post(r'https://api.nal.usda.gov/fdc/v1/foods/search', params=params, json=data)
    result = response.json()

    item_description = result['foods'][0]['description']

    item_label.config(text=item_description)

    add_to_plate_btn = tk.Button(search_result_frame, text="Add To Plate", font=40, command=lambda: add_to_plate(item_label))
    add_to_plate_btn.place(relx=0.4, rely=0.63, relheight=0.33, relwidth=0.2)

    # for i in range(8):
    #     nutrient_name = result['foods'][0]['foodNutrients'][i]['nutrientName']
    #     nutrient_value = result['foods'][0]['foodNutrients'][i]['value']
    #     nutrient_unit_name = result['foods'][0]['foodNutrients'][i]['unitName']
    #
    #     print(nutrient_name + ': ' + str(nutrient_value) + ' ' + nutrient_unit_name)



def add_to_plate():
    whatever = 'whatever'




root = tk.Tk()  # referring to the screen

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

# title()
# plate_image()
# food_search()
# search_result_area()
# nutrient_images()




my_font = Font(family="Helvetica", size=55, weight="bold")
label1 = tk.Label(root, text="Perfect Plate", font=my_font, fg="#ff4d4d")
label1.place(relx=0.5, relwidth=.9, relheight=.1, anchor='n')




plate_image = ImageTk.PhotoImage(file='plate.png')  # plate image
plate_label = tk.Label(root, image=plate_image)
plate_label.place(relx=0.35, rely=0.075, relwidth=.3, relheight=.2)



#


top_frame = tk.Frame(root, bg='#9cc098', bd=5)  # The top section, green background, border = 5
top_frame.place(relx=0.5, rely=0.26, relwidth=0.5, relheight=0.045, anchor='n')

food_entry = tk.Entry(top_frame, font=40, bd=3)  # text box
food_entry.place(relwidth=.57, relheight=1)

button = tk.Button(top_frame, text="Search", font=40, command=lambda: get_data(food_entry.get()))
button.place(relx=0.6, rely=0.04, relheight=1, relwidth=0.4)



# The Search result

search_result_frame = tk.Frame(root, bg='#9cc098')  # The bottom section,
search_result_frame.place(relx=0.5, rely=0.31, relwidth=.98, relheight=0.12, anchor='n')

search_result_font = Font(family="Helvetica", size=30, weight="bold")
item_label = tk.Label(search_result_frame, text="Enter An Item", font=search_result_font, bg='#9cc098',
                      fg="#f2f2f2")
item_label.place(relwidth=.98, relheight=.45)



# The bottom section

bottom_frame = tk.Frame(root)
bottom_frame.place(relx=0.5, rely=0.43, relwidth=.98, relheight=0.16, anchor='n')

carbs_image = ImageTk.PhotoImage(file='carbs.png')  # carbs image
carbs_image_label = tk.Label(bottom_frame, image=carbs_image)
carbs_image_label.place(relx=0.1, rely=0.0, relwidth=0.2, relheight=1)

protein_image = ImageTk.PhotoImage(file='protein.png')  # protein image
protein_image_label = tk.Label(bottom_frame, image=protein_image)
protein_image_label.place(relx=0.4, rely=0.0, relwidth=0.2, relheight=1)

fat_image = ImageTk.PhotoImage(file='fat.png')  # fat image
fat_label = tk.Label(bottom_frame, image=fat_image)
fat_label.place(relx=0.7, rely=0.0, relwidth=0.2, relheight=1)


# meal_frame = tk.Frame(root, bg='#d1e2d0', bd=10)                               # The next section,
# meal_frame.place(relx=0.5, rely=0.5, relwidth=.98, relheight=0.05, anchor='n')
#
# lowerFont = Font(family="Helvetica", size=30, weight="bold")
# label3 = tk.Label(meal_frame, text="yeah", font=lowerFont, bg='#9cc098', fg="#f2f2f2")
# label3.place(relwidth=.98, relheight=.45)



root.mainloop()

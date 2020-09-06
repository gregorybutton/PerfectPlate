class FoodItem:
    def __init__(self, description, carbs, protein, fat):
        self.description = description
        self.carbs = carbs
        self.protein = protein
        self.fat = fat

    def get_name(self):
        return self.description

    def get_carbs(self):
        return self.carbs

    def get_protein(self):
        return self.protein

    def get_fat(self):
        return self.fat

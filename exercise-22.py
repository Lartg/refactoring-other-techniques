class Recipe:
  def __init__(self, name, prep_time = None, is_veggie = None, food_type = None, ingredients = None, instructions = None):
      self.name = name
      self.prep_time = prep_time
      self.is_veggie = is_veggie
      self.food_type = food_type
      self.ingredients = ingredients
      self.instructions = instructions
  def print_recipe(self):
    for key, value in self.__dict__.items():
      print(key, value)

if __name__ == "__main__":
  recipe = Recipe('name')
  recipe.print_recipe()
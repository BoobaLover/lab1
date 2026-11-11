
import unittest


class Ingredient:
    def __init__(self, name, quantity, unit):
        self.name = name
        self.quantity = quantity
        self.unit = unit

    def __str__(self):
        return f"{self.name} — {self.quantity} {self.unit}"


class Recipe:
    def __init__(self, name, description, cooking_time):
        self.id = None
        self.name = name
        self.description = description
        self.cooking_time = cooking_time
        self.ingredients = []
        self.steps = []

    def add_ingredient(self, ingredient):
        self.ingredients.append(ingredient)

    def remove_ingredient(self, name):
        for ingredient in self.ingredients:
            if ingredient.name.lower() == name.lower():
                self.ingredients.remove(ingredient)
                return True
        return False

    def add_step(self, step):
        self.steps.append(step)

    def show_recipe(self):
        print(f"\nРецепт: {self.name}")
        print(f"Описание: {self.description}")
        print(f"Время приготовления: {self.cooking_time} минут")

        print("\nИнгредиенты:")
        for ingredient in self.ingredients:
            print(ingredient)

        print("\nПриготовление:")
        for number, step in enumerate(self.steps, start=1):
            print(f"{number}. {step}")


class Cookbook:
    def __init__(self, name):
        self.name = name
        self.recipes = []
        self.next_id = 1

    def add_recipe(self, recipe):
        recipe.id = self.next_id
        self.next_id += 1
        self.recipes.append(recipe)
        return recipe.id

    def get_recipe(self, recipe_id):
        for recipe in self.recipes:
            if recipe.id == recipe_id:
                return recipe
        return None

    def get_all_recipes(self):
        return self.recipes.copy()

    def find_recipe(self, name):
        for recipe in self.recipes:
            if recipe.name.lower() == name.lower():
                return recipe
        return None

    def update_recipe(self, recipe_id, name=None,
                      description=None, cooking_time=None):
        recipe = self.get_recipe(recipe_id)

        if recipe is None:
            return False

        if name is not None:
            recipe.name = name

        if description is not None:
            recipe.description = description

        if cooking_time is not None:
            recipe.cooking_time = cooking_time

        return True

    def delete_recipe(self, recipe_id):
        recipe = self.get_recipe(recipe_id)

        if recipe is None:
            return False

        self.recipes.remove(recipe)
        return True

    def show_recipes(self):
        print(f"\nКулинарная книга: {self.name}")

        for recipe in self.recipes:
            print(f"{recipe.id}. {recipe.name}")


class TestCookbook(unittest.TestCase):
    def setUp(self):
        self.cookbook = Cookbook("Тестовая книга")
        self.recipe = Recipe("Паста", "Паста с сыром", 25)
        self.recipe_id = self.cookbook.add_recipe(self.recipe)

    def test_add_recipe(self):
        self.assertEqual(len(self.cookbook.get_all_recipes()), 1)

    def test_get_recipe(self):
        result = self.cookbook.get_recipe(self.recipe_id)
        self.assertEqual(result.name, "Паста")

    def test_find_recipe(self):
        result = self.cookbook.find_recipe("Паста")
        self.assertIsNotNone(result)

    def test_update_recipe(self):
        self.cookbook.update_recipe(self.recipe_id, name="Пицца")
        result = self.cookbook.get_recipe(self.recipe_id)
        self.assertEqual(result.name, "Пицца")

    def test_delete_recipe(self):
        self.cookbook.delete_recipe(self.recipe_id)
        self.assertIsNone(self.cookbook.get_recipe(self.recipe_id))

    def test_delete_missing_recipe(self):
        result = self.cookbook.delete_recipe(999)
        self.assertFalse(result)

    def test_add_ingredient(self):
        ingredient = Ingredient("Сыр", 100, "г")
        self.recipe.add_ingredient(ingredient)
        self.assertEqual(len(self.recipe.ingredients), 1)

    def test_remove_ingredient(self):
        ingredient = Ingredient("Сыр", 100, "г")
        self.recipe.add_ingredient(ingredient)
        result = self.recipe.remove_ingredient("Сыр")
        self.assertTrue(result)
        self.assertEqual(len(self.recipe.ingredients), 0)



def main():
    cookbook = Cookbook("Мои рецепты")

    # Добавляем готовые рецепты

    pasta = Recipe(
        "Паста с сыром",
        "Паста в сливочном соусе с сыром",
        25
    )
    pasta.add_ingredient(Ingredient("Макароны", 200, "г"))
    pasta.add_ingredient(Ingredient("Сыр", 100, "г"))
    pasta.add_ingredient(Ingredient("Сливки", 150, "мл"))
    pasta.add_step("Отварить макароны")
    pasta.add_step("Разогреть сливки")
    pasta.add_step("Добавить сыр и перемешать")
    pasta.add_step("Соединить соус с макаронами")
    cookbook.add_recipe(pasta)

    pancakes = Recipe(
        "Блины",
        "Тонкие домашние блины",
        40
    )
    pancakes.add_ingredient(Ingredient("Молоко", 500, "мл"))
    pancakes.add_ingredient(Ingredient("Мука", 200, "г"))
    pancakes.add_ingredient(Ingredient("Яйца", 2, "шт"))
    pancakes.add_ingredient(Ingredient("Сахар", 30, "г"))
    pancakes.add_step("Смешать яйца, сахар и молоко")
    pancakes.add_step("Добавить муку и перемешать")
    pancakes.add_step("Обжарить блины с двух сторон")
    cookbook.add_recipe(pancakes)

    salad = Recipe(
        "Овощной салат",
        "Лёгкий салат из свежих овощей",
        15
    )
    salad.add_ingredient(Ingredient("Помидоры", 200, "г"))
    salad.add_ingredient(Ingredient("Огурцы", 150, "г"))
    salad.add_ingredient(Ingredient("Оливковое масло", 15, "мл"))
    salad.add_step("Нарезать овощи")
    salad.add_step("Смешать ингредиенты")
    salad.add_step("Заправить маслом")
    cookbook.add_recipe(salad)

    # Главное меню

    while True:
        print("\n=== КУЛИНАРНАЯ КНИГА ===")
        print("1. Добавить рецепт")
        print("2. Показать все рецепты")
        print("3. Найти рецепт")
        print("4. Изменить рецепт")
        print("5. Удалить рецепт")
        print("6. Выход")

        choice = input("\nВыберите действие: ")

        if choice == "1":
            name = input("Название рецепта: ")
            description = input("Описание: ")

            try:
                cooking_time = int(input("Время приготовления (минуты): "))
            except ValueError:
                print("Время должно быть числом.")
                continue

            recipe = Recipe(name, description, cooking_time)

            while True:
                ingredient_name = input(
                    "\nНазвание ингредиента (Enter для завершения): "
                )

                if ingredient_name == "":
                    break

                try:
                    quantity = float(input("Количество: "))
                except ValueError:
                    print("Количество должно быть числом.")
                    continue

                unit = input("Единица измерения: ")

                recipe.add_ingredient(
                    Ingredient(ingredient_name, quantity, unit)
                )

            while True:
                step = input(
                    "\nШаг приготовления (Enter для завершения): "
                )

                if step == "":
                    break

                recipe.add_step(step)

            recipe_id = cookbook.add_recipe(recipe)
            print(f"Рецепт добавлен. Его ID: {recipe_id}")

        elif choice == "2":
            cookbook.show_recipes()

        elif choice == "3":
            name = input("Введите название рецепта: ")
            recipe = cookbook.find_recipe(name)

            if recipe:
                recipe.show_recipe()
            else:
                print("Рецепт не найден.")

        elif choice == "4":
            try:
                recipe_id = int(input("Введите ID рецепта: "))
            except ValueError:
                print("ID должен быть числом.")
                continue

            recipe = cookbook.get_recipe(recipe_id)

            if recipe is None:
                print("Рецепт не найден.")
                continue

            print("Оставьте поле пустым, если не хотите его менять.")

            name = input("Новое название: ")
            description = input("Новое описание: ")
            cooking_time = input("Новое время приготовления: ")

            if cooking_time == "":
                cooking_time = None
            else:
                try:
                    cooking_time = int(cooking_time)
                except ValueError:
                    print("Время должно быть числом.")
                    continue

            cookbook.update_recipe(
                recipe_id,
                name=name if name else None,
                description=description if description else None,
                cooking_time=cooking_time
            )

            print("Рецепт обновлён.")

        elif choice == "5":
            try:
                recipe_id = int(input("Введите ID рецепта: "))
            except ValueError:
                print("ID должен быть числом.")
                continue

            if cookbook.delete_recipe(recipe_id):
                print("Рецепт удалён.")
            else:
                print("Рецепт не найден.")

        elif choice == "6":
            print("До свидания!")
            break

        else:
            print("Неверный пункт меню. Попробуйте ещё раз.")


if __name__ == "__main__":
    main()

#python -m unittest main -v
#
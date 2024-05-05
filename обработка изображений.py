from PIL import Image, ImageFilter

# Функция для изменения размера изображения
def resize_image(input_image, output_image, new_width, new_height):
    img = Image.open(input_image)
    resized_img = img.resize((new_width, new_height))
    resized_img.save(output_image)
    print(f"Изображение успешно изменено размера до {new_width}x{new_height}.")

# Функция для применения фильтра к изображению
def apply_filter(input_image, output_image, filter_type):
    img = Image.open(input_image)
    filtered_img = img.filter(filter_type)
    filtered_img.save(output_image)
    print(f"Применен фильтр {filter_type} к изображению.")

if __name__ == "__main__":
    # Изменение размера изображения
    resize_image("input.jpg", "resized_output.jpg", 800, 600)

    # Применение фильтра к изображению
    apply_filter("input.jpg", "filtered_output.jpg", ImageFilter.BLUR)

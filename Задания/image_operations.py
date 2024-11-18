from PIL import Image

def process_image(image_path, new_width, new_height, rotation_angle):
    try:
        with Image.open(image_path) as img:
            # Изменение размера
            resized_img = img.resize((new_width, new_height))
            # Поворот изображения
            rotated_img = resized_img.rotate(rotation_angle, expand=True)
            # Сохранение обработанного изображения
            processed_path = "processed_image.png"
            rotated_img.save(processed_path)
            return processed_path
    except Exception as e:
        raise RuntimeError(f"Ошибка обработки изображения: {e}")

import timeit
import subprocess
from image_operations import process_image
from PIL import Image
import os

def test_main():
    """Запускает main.py как отдельный процесс для замера времени"""
    subprocess.run(["python", "main.py"], check=True)

def test_process_image():
    """Измеряет скорость выполнения функции process_image"""
    # Подготовка тестового изображения
    test_image_path = "test_image.jpg"
    if not os.path.exists(test_image_path):
        with Image.new("RGB", (1000, 1000), color="blue") as img:
            img.save(test_image_path)
    
    # Запуск теста
    process_image(test_image_path, 500, 500, 45)
    os.remove("processed_image.png")  # Очистка после теста

def run_tests():
    print("=== Тестирование скорости ===")
    print("1. Замер скорости всей программы:")
    total_time = timeit.timeit("test_main()", setup="from __main__ import test_main", number=1)
    print(f"Время выполнения: {total_time:.4f} секунд\n")

    print("2. Замер скорости функции process_image:")
    process_time = timeit.timeit("test_process_image()", setup="from __main__ import test_process_image", number=5)
    print(f"Среднее время выполнения: {process_time / 5:.4f} секунд\n")

if __name__ == "__main__":
    run_tests()

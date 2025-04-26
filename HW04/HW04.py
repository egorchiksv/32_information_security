import hashlib

def compute_file_hash(file_path, algorithm='sha256'):
    """Compute the hash of a file using the specified algorithm."""
    hash_func = hashlib.new(algorithm)
    
    with open(file_path, 'rb') as file:
        while chunk := file.read(8192):
            hash_func.update(chunk)
    
    return hash_func.hexdigest()

def main():
    file_path = input("Введите путь к файлу и его имя: ")
    algorithm = input("Выберете хеш-функцию (e.g., md5, sha1, sha256): ")
    
    try:
        file_hash = compute_file_hash(file_path, algorithm)
        print(f"The {algorithm} hash of the file is: {file_hash}")
    except FileNotFoundError:
        print("Файл не найден. Пожалуйста, введите правильный путь к файлу.")
    except ValueError:
        print(f"Неверный алгоритм хеширования: {algorithm}. Пожалуйста, введите правильный алгоритм (e.g., md5, sha1, sha256).")

if __name__ == "__main__":
    main()
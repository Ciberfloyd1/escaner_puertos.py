import hashlib
import argparse

def hash_password(password, algorithm='md5'):
    """Hashea una contraseña usando el algoritmo especificado."""
    if algorithm == 'md5':
        return hashlib.md5(password.encode()).hexdigest()
    elif algorithm == 'sha1':
        return hashlib.sha1(password.encode()).hexdigest()
    elif algorithm == 'sha256':
        return hashlib.sha256(password.encode()).hexdigest()
    else:
        raise ValueError("Algoritmo de hash no soportado")

def crack_hash(target_hash, wordlist_file, algorithm='md5'):
    """Intenta descifrar un hash usando un archivo de diccionario."""
    print(f"Intentando descifrar el hash: {target_hash}")
    print(f"Usando algoritmo: {algorithm}")
    
    try:
        with open(wordlist_file, 'r', encoding='utf-8', errors='ignore') as f:
            for line in f:
                word = line.strip()
                hashed_word = hash_password(word, algorithm)
                if hashed_word == target_hash:
                    return word
    except FileNotFoundError:
        print(f"Error: No se pudo encontrar el archivo de diccionario '{wordlist_file}'")
    except Exception as e:
        print(f"Error al leer el archivo de diccionario: {e}")
    
    return None

def main():
    parser = argparse.ArgumentParser(description="Descifrador de hash con diccionario")
    parser.add_argument("hash", help="El hash a descifrar")
    parser.add_argument("wordlist", help="Archivo de diccionario a usar")
    parser.add_argument("--algorithm", choices=['md5', 'sha1', 'sha256'], default='md5',
                        help="Algoritmo de hash (default: md5)")
    
    args = parser.parse_args()

    result = crack_hash(args.hash, args.wordlist, args.algorithm)
    
    if result:
        print(f"¡Hash descifrado! La contraseña es: {result}")
    else:
        print("No se pudo descifrar el hash con el diccionario proporcionado.")

if __name__ == "__main__":
    main()

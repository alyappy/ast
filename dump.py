import os
import sys
import re

def read_ast_file(file_path):
    """Membaca isi file AST dan mengembalikannya sebagai string."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"[ERROR] Gagal membaca file: {e}")
        return None

def extract_and_format_ja_text(content):
    """ Mengekstrak teks dalam blok 'ja={...}' dan memformatnya sesuai keinginan user. """
    pattern = re.compile(r'ja\s*=\s*\{(.*?)\n\s*\},', re.DOTALL)
    matches = pattern.findall(content)

    formatted_texts = []
    for match in matches:
        formatted_block = f"ja={{\n{{\n{match.strip()},\n}},\n}},\n"
        formatted_texts.append(formatted_block)

    return "\n".join(formatted_texts)

def process_ast_file(input_filename):
    """ Memproses file AST, mengekstrak teks 'ja={...}', dan menyimpannya dalam file baru """
    content = read_ast_file(input_filename)
    if not content:
        print("[ERROR] Tidak bisa membaca file!")
        return
    
    formatted_output = extract_and_format_ja_text(content)

    output_filename = input_filename.replace(".ast", "_formatted.ast")
    with open(output_filename, "w", encoding="utf-8") as f:
        f.write(formatted_output)

    print(f"[SUCCESS] Hasil disimpan di: {output_filename}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Gunakan: py dump.py <nama_file.ast>")
    else:
        process_ast_file(sys.argv[1])

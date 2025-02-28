import os
import re

def read_ast_file(file_path):
    """Membaca isi file AST dan mengembalikannya sebagai string."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.read()
    except Exception as e:
        print(f"[ERROR] Gagal membaca file: {e}")
        return None

def merge_formatted_text(original_content, formatted_content):
    """Mengganti blok ja={...} dalam file asli dengan versi yang sudah diformat."""
    pattern = re.compile(r'ja\s*=\s*\{(.*?)\n\s*\},', re.DOTALL)
    matches = pattern.findall(original_content)

    formatted_blocks = formatted_content.strip().split("\n\n")

    if len(matches) != len(formatted_blocks):
        print("[WARNING] Jumlah blok tidak cocok, mungkin ada yang hilang atau ekstra.")

    def replacer(match):
        if formatted_blocks:
            return formatted_blocks.pop(0)
        return match.group(0)

    merged_content = pattern.sub(replacer, original_content)
    return merged_content

def main():
    original_file = input("Masukkan file asli (.ast): ").strip()
    formatted_file = input("Masukkan file hasil dump (.ast): ").strip()

    if not os.path.exists(original_file):
        print(f"[ERROR] File tidak ditemukan: {original_file}")
        return
    if not os.path.exists(formatted_file):
        print(f"[ERROR] File tidak ditemukan: {formatted_file}")
        return

    original_content = read_ast_file(original_file)
    formatted_content = read_ast_file(formatted_file)

    if original_content and formatted_content:
        merged_content = merge_formatted_text(original_content, formatted_content)
        merged_filename = original_file.replace(".ast", "_merged.ast")
        with open(merged_filename, "w", encoding="utf-8") as f:
            f.write(merged_content)

        print(f"[SUCCESS] Hasil gabungan disimpan di: {merged_filename}")

if __name__ == "__main__":
    main()

import json
import os

def convert_passwords_to_json_array(input_path="passwords.txt", output_path="output.txt"):
    """
    Converts a newline-separated wordlist into a single-line JSON array 
    for bypassing multi-credential authentication limit controls.
    """
    if not os.path.exists(input_path):
        print(f"[-] Error: Input file '{input_path}' not found.")
        return

    try:
        # Reading passwords from raw wordlist
        with open(input_path, "r", encoding="utf-8") as f:
            password_list = [line.strip() for line in f if line.strip()]

        # Converting python list into clean single-line JSON structure
        json_payload = json.dumps(password_list)

        # Saving the formatted payload
        with open(output_path, "w", encoding="utf-8") as out_f:
            out_f.write(json_payload)

        print(f"[+] Success: Formatted payload saved to '{output_path}'")
        print(f"[+] Total passwords processed: {len(password_list)}")
        
    except Exception as e:
        print(f"[-] Unexpected error occurred: {str(e)}")

if __name__ == "__main__":
    convert_passwords_to_json_array()

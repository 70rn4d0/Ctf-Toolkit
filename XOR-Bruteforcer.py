def xor_bruteforce(ciphertext):
    for key in range(256):
        decoded = ''.join(chr(b ^ key) for b in ciphertext)
        if "flag{" in decoded:  # Common CTF flag pattern
            print(f"Key: {key}, Flag: {decoded}")

xor_bruteforce(b'\x23\x20\x25\x26')  # Example ciphertext

#!/bin/python3
import base64

def hex_to_base64(hex_str):
    bytes_data = bytes.fromhex(hex_str)
    return base64.b64encode(bytes_data).decode()

print(hex_to_base64("48656c6c6f"))  # Hello

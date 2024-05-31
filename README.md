import base64

def encode_to_base64(text):
    encoded_bytes = base64.b64encode(text.encode('utf-8'))
    encoded_text = encoded_bytes.decode('utf-8')
    return encoded_text

def main():
    text_to_encode = input("Enter the ID to encode: ")
    encoded_text = encode_to_base64(text_to_encode)
    print("Encoded ID:", encoded_text)

if __name__ == "__main__":
    main()

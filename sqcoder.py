import urllib.parse
import base64

def encode_payloads(payloads, encoding_type):
    if not isinstance(payloads, list):
        return 1  
    
    encoded_payloads = []
    
    for payload in payloads:
        try:
            if encoding_type.lower() == 'url':
                encoded_payload = urllib.parse.quote(payload)
            elif encoding_type.lower() == 'base64':
                encoded_payload = base64.b64encode(payload.encode('utf-8')).decode('utf-8')
            else:
                return 2  # Error code 2: Invalid encoding type
            encoded_payloads.append(encoded_payload)
        except Exception as e:
            return 3  

    return encoded_payloads

# Example usage
if __name__ == "__main__":
  
    payloads = input("Enter SQLi payloads separated by commas: ").split(',')

    # Choose encoding type
    encoding_type = input("Choose encoding type ('url' or 'base64'): ").strip().lower()

  
    result = encode_payloads(payloads, encoding_type)

    if isinstance(result, list):
        print("\nEncoded Payloads:")
        for idx, payload in enumerate(result, 1):
            print(f"{idx}. {payload}")
    else:
        print(f"Error occurred: Error code {result}")

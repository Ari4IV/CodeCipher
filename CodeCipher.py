def text_to_binary(text):
    # 將文字轉換為二進位，使用UTF-8編碼
    binary_representation = ''.join(format(byte, '08b') for byte in text.encode('utf-8'))
    return binary_representation

def binary_to_text(binary_string):
    # 將二進位轉換為文字，還原為UTF-8編碼後解碼
    bytes_array = bytearray()
    for i in range(0, len(binary_string), 8):
        byte = binary_string[i:i+8]
        bytes_array.append(int(byte, 2))
    text = bytes_array.decode('utf-8')
    return text

def main():
    while True:
        print("選擇操作：")
        print("1. 文字轉換為二進位")
        print("2. 二進位轉換為文字")
        print("3. 離開")
        choice = input("請選擇(1/2/3): ")
        
        if choice == '1':
            text = input("輸入要轉換為二進位的文字: ")
            binary = text_to_binary(text)
            print(f"文字的二進位表示為: {binary}")
        elif choice == '2':
            binary_string = input("輸入要轉換為文字的二進位字串: ")
            try:
                text = binary_to_text(binary_string)
                print(f"二進位轉換後的文字為: {text}")
            except Exception as e:
                print(f"轉換失敗捏，錯誤訊息：{e}")
        elif choice == '3':
            print("已離開程式捏。")
            break
        else:
            print("無效的選項，請重新選擇捏。")

if __name__ == "__main__":
    main()

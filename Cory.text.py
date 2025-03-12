def convert_text():
    print("أداة تحويل النصوص")
    text = input("أدخل النص الذي تريد تحويله: ")

    print("\nاختر الخيار الذي تود تطبيقه:")
    print("1 - تحويل النص إلى أحرف كبيرة")
    print("2 - تحويل النص إلى أحرف صغيرة")

    choice = input("أدخل الخيار (1 أو 2): ")

    if choice == '1':
        print("النص بعد التحويل إلى أحرف كبيرة: ", text.upper())
    elif choice == '2':
        print("النص بعد التحويل إلى أحرف صغيرة: ", text.lower())
    else:
        print("خيار غير صالح. يرجى اختيار 1 أو 2.")

if __name__ == "__main__":
    convert_text()

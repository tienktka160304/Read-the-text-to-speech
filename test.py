import pyttsx3

# Khởi tạo đối tượng pyttsx3
engine = pyttsx3.init()

# Chức năng chuyển đổi văn bản thành giọng nói
def text_to_speech(text):
    engine.say(text)
    engine.runAndWait()

# Chọn giọng nói (nam hoặc nữ)
voices = engine.getProperty('voices')

# Giọng nam: 0, Giọng nữ: 1

print("Hãy chọn giọng mà bạn muốn: 1:Giọng nữ   0:Giọng nam")
t = int(input())
engine.setProperty('voice', voices[t].id)
# Tốc độ giọng nói (mặc định là 200, có thể điều chỉnh)

print("Hãy chọn tốc độ đọc mà bạn muốn:")
x = int(input())
engine.setProperty('rate', x)  # Chỉnh tốc độ chậm lại

# Nhập văn bản cần chuyển đổi
text = input("Nhập văn bản bạn muốn chuyển thành giọng nói: ")

# Gọi hàm chuyển đổi văn bản thành giọng nói
text_to_speech(text)

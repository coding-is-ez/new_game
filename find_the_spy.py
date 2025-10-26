from guizero import App, Text, Box, info, PushButton, Picture
from random import choice
import PIL

window = App(title = "Find the spy", layout = "grid")

gened_box = Box(window, layout = "grid", grid = [0, 0], border = 5)

persons = []

very_sussy = ["very_sus.png", "job.png"]

def correct(a: int, b: int, spy_button: PushButton):
        global very_sussy
        info(title = "Congratulations!", text = "You guessed correctly!")
        spy_button.destroy()
        pic = Picture(gened_box, image = choice(very_sussy), grid = [a, b])
        pic.resize(width = 175, height = 175)
        
def wrong():
    global btn
    info(title = "FAHHH!!!!", text = "WRONG! GUESS AGAIN!")
    btn.text_color = "red"

def back_to_zero():
    global count, spy, persons # Làm cho các biến toàn cục được sử dụng trong hàm
    count = 0
    for widget in gened_box.children():
        widget.destroy()

    for i in range(4):
        for j in range(4):
            btn = PushButton(gened_box, grid = [i, j], text = "?" , width = 20, height = 10) # Tái tạo lại grid sau khi phá hủy
            btn.update_command(guess, args = [i, j, btn]) 
            persons.append([i, j])

# Tạo grid lần đầu

count = 0

def guess(a: int, b: int, spy_button: PushButton):
    global count
    global spy
    global persons
    if [a, b] == spy:
        correct(a, b, spy_button)
    else:
        wrong()
    
    count += 1

    if count == 5:
        info(title = "dmm choi ngu the", text = "U LOSE! LOL")

for i in range(4):
    for j in range(4):
        btn = PushButton(gened_box, grid = [i, j], text = "?" , width = 20, height = 10)
        btn.update_command(guess, args = [i, j, btn]) # Cập nhật lệnh cho Pushbutton với hàm và vị trí trong grid tương ứng
        persons.append([i, j])

retry_btn = PushButton(window, grid = [0, 5], command = back_to_zero)

spy = choice(persons)
print("The first spy is:" ,spy)

# Run app
window.display()
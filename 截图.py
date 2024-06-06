import pyautogui
import keyboard


def move_mouse2():
    # 获取当前鼠标位置
    current_position = pyautogui.position()

    # 计算新位置
    new_position = (current_position.x + 200, current_position.y + 200)
    # 移动鼠标到新位置
    pyautogui.moveTo(new_position)

def move_mouse5():
    # 获取当前鼠标位置
    current_position = pyautogui.position()

    # 计算新位置
    new_position = (current_position.x + 500, current_position.y + 500)

    # 移动鼠标到新位置
    pyautogui.moveTo(new_position)
def move_mouse4():
    # 获取当前鼠标位置
    current_position = pyautogui.position()

    # 计算新位置
    new_position = (current_position.x + 400, current_position.y + 400)

    # 移动鼠标到新位置
    pyautogui.moveTo(new_position)
def move_mouse3():
    # 获取当前鼠标位置
    current_position = pyautogui.position()

    # 计算新位置
    new_position = (current_position.x + 300, current_position.y + 300)

    # 移动鼠标到新位置
    pyautogui.moveTo(new_position)

while True:
    # 监听键盘事件
    if keyboard.is_pressed('3'):
        move_mouse3()
    if keyboard.is_pressed('4'):
        move_mouse4()
    if keyboard.is_pressed('2'):
        move_mouse2()
    if keyboard.is_pressed('5'):
        move_mouse5()
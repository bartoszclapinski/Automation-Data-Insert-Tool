import pyautogui as pag
import time


def wait(wait_in_seconds):
    time.sleep(wait_in_seconds)


def automate_keyboard_actions(data_series, update_func):
    try:
        update_func('Waiting 5s to start\n')
        wait(5)
        update_func('Starting...\n')
        wait(2)

        for data in data_series:
            update_func('Writing data\n')
            pag.write(str(data))
            wait(2)

            update_func('Pressing enter\n')
            pag.press('enter')
            wait(2)

    except Exception as e:
        update_func(f"Error: {e}\n")

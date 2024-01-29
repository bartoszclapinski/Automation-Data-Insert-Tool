import pyautogui as pag
import time


def wait(wait_in_seconds):
    time.sleep(wait_in_seconds)


def automate_test(data_series, update_func):
    try:
        update_func('Waiting 5s to start\n')
        wait(5)
        update_func('Starting...')
        wait(2)

        for data in data_series:
            if str(data).lower() == 'nan':
                return
            else:
                pag.write(str(data))
                wait(0.5)
                pag.press('enter')
                wait(0.5)

    except KeyboardInterrupt as error:
        update_func(f"Error: {error}\n")


def automate_keyboard_actions(data_series, update_func):
    try:
        update_func('Waiting 5s to start\n')
        wait(5)
        update_func('Starting...\n')
        wait(2)

        for data in data_series:
            update_func('Writing data\n')
            pag.press('f9')
            wait(1)
            pag.press('f2')
            wait(1)
            pag.press('down')
            wait(1)
            pag.press('down')
            wait(1)
            pag.press('down')
            wait(1)
            pag.press('enter')
            wait(1)
            pag.press('tab')
            wait(1)

            pag.write(str(data))
            wait(1)
            pag.press('tab')
            wait(1)
            pag.write(str(data))
            wait(1)
            pag.press('tab')
            wait(1)
            pag.write('1')
            wait(0.7)
            pag.press('tab')
            wait(0.7)
            pag.press('tab')
            wait(1)

            # f9 f2 down down down enter tab insert tab insert tab 1 tab tab

    except Exception as e:
        update_func(f"Error: {e}\n")

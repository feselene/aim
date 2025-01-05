import pydirectinput # type: ignore
import time

def main():
    time.sleep(1)
    while True:
        # Press 'R' key once
        pydirectinput.press('r')
        print("Pressed 'R'")
        time.sleep(2)
        pydirectinput.keyDown('t')
        time.sleep(1)
        pydirectinput.keyUp('t')
        for i in range(40):
            pydirectinput.keyDown('d')
            time.sleep(0.5)
            pydirectinput.keyUp('d')   
            pydirectinput.keyDown('a')
            time.sleep(0.5)
            pydirectinput.keyUp('a')  
        time.sleep(5)  # Adjust as needed

if __name__ == "__main__":
    main()

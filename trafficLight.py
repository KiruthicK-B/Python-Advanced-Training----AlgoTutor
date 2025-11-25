import time
from datetime import datetime


DAY_START = 6      
DAY_END   = 22     

GREEN_TIME = 5
YELLOW_TIME = 2
RED_TIME = 5
NIGHT_BLINK_TIME = 1

DIRECTIONS = ["North", "South", "East", "West"]

def is_day_time():
    """Check if current time is day."""
    now = datetime.now().hour
    return DAY_START <= now < DAY_END

def show_signal(direction, red, yellow, green):
    """Display lights for a direction."""
    print(f"\n[{direction} Signal]")
    print(f"RED   : {'ON' if red else 'OFF'}")
    print(f"YELLOW: {'ON' if yellow else 'OFF'}")
    print(f"GREEN : {'ON' if green else 'OFF'}")

def day_mode_cycle():
    """Normal day mode cycle for all 4 signals."""
    for direction in DIRECTIONS:
        print("\n======================================")
        print(f" DAY MODE - Traffic Flow for {direction}")

        """Normal day mode cycle for all 4 signals."""
        print("======================================")  
        show_signal(direction, red=False, yellow=False, green=True)
        time.sleep(GREEN_TIME)

        show_signal(direction, red=False, yellow=True, green=False)
        time.sleep(YELLOW_TIME)

        show_signal(direction, red=True, yellow=False, green=False)
        time.sleep(RED_TIME)


def night_mode_blink():
    """Night mode – blinking yellow for all."""
    print("\n======================================")
    print(" NIGHT MODE - Low Traffic (Blinking Yellow)")
    print("======================================")

    for direction in DIRECTIONS:
        show_signal(direction, red=False, yellow=True, green=False)

    time.sleep(NIGHT_BLINK_TIME)

if __name__ == "__main__":

    print("🚦 Traffic Light System Started\n")

    while True:
        if is_day_time():
            day_mode_cycle()
        else:
            night_mode_blink()

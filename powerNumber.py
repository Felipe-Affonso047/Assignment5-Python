#!/usr/bin/env python3

# Created by: Felipe Garcia Affonso
# Created on: May 2021
# This program does power


def main():
    # This function does power
    try:
        print("Enter 2 numbers, the second one will"
              " be the power of the second one. xʸ")
        base = int(input("x: "))
        power = int(input("y: "))
        power_to_show = power
        result = 1

        if power > 0:
            while power > 0:
                power = power - 1
                result = result * base
        elif power < 0:
            while power < 0:
                power = power + 1
                result = result / base

        print("{0} to the power of {1} equal {2}"
              .format(base, power_to_show, result))
    except Exception:
        print("\nThis input is invalid, please, insert an integer")
    finally:
        print("\nDone.")


if __name__ == "__main__":
    main()

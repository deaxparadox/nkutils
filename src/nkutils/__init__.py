import argparse 

def arguments():
    arg = argparse.ArgumentParser()
    arg.add_argument("-n", type=int, help="Just a number")
    return arg.parse_args()


def draw_car():
    print("\n\tLet's go for a ride\n")
    car = r"""
        ______
       /|_||_\`.__
      (   _    _ _\
      =`-(_)--(_)-'
    """
    print(car)


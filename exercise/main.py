import c
#import a.a2.hello as hello
from a.a2.hello import hello
from b.random_number_generator import generate_number_between, generate_until_drawn
from a import try_again
from a.a1.number_generator import *


def thank_you():
    print("Thank you. Good bye.")


def lotto():
    """

    :return:
    """
    playing = True
    hello()
    #print(generate_until_drawn.__doc__)

    while playing:
        number = c.retrieve_number_from_user()
        times = generate_until_drawn(number, 1, 100)
        c.inform_about_the_result(times)
        c.get_reward(times)
        playing = try_again()


    thank_you()


if __name__ == "__main__":
    lotto()

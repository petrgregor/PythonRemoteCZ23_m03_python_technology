def get_reward(times):
    if times <= 10:
        print("Congratulations, you won a car!")
    elif 10 < times <= 25:
        print("Congratulations, you won the trip!")
    elif 25 < times <= 50:
        print("Congratulations, you won the consolation prize!")
    else:
        print("Unfortunately, maybe next time you'll get lucky...")
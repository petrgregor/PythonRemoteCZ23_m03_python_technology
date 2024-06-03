def try_again():
    vote = input("\nDo you want to try again? (A/a/Y/y - Yes; N/n - No): ")
    votes_map = {
        "A": True,
        "a": True,
        "Y": True,
        "y": True,
        "N": False,
        "n": False
    }

    return votes_map[vote]

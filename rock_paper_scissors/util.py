"""
The main logic of the game are described in this modeule
"""
OPTIONS = ["Rock", "Scissors", "Paper"]

def verify(option):
    """
    Verify if the given option is valid
        Args:
            option (str) shlould be Rock, Paper or Scissors

        Returns:
            True if the ptions is Rock, Paper or Scissors

        Raises:
            ValueError: If `option` is not on `OPTIONS`

    """
    pass


def match(player1, player2):
    """
    Determin if the player1 win in base of the choose of each
    player, the paremerts are the follwoing:
        Args:
            player1 (str) shlould be Rock, Paper or Scissors
            player2 (str) shlould be Rock, Paper or Scissors

        Returns:
            1 if player1 win, 2 if player2 win and 0 if they tie


    """
    pass

def get_computer():
    """
        Returns:
            A random valid option for the game
    """
    pass

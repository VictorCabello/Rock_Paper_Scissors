""" This module expose a rest api to play a game """
from connexion import App
from waitress import serve

APP = App(__name__, specification_dir='swagger/')



def match(player):
    """
    Start a match vs a computer and return the output
    """
    computer = 'Rock' # TODO: add logic to get random choise
    match_output =  1 # TODO: resolve the match
    match_output_str = ''
    if match_output == 1:
        match_output_str = 'The player win'
    elif match_output == 2:
        match_output_str = 'The computer win'
    elif match_output == 0:
        match_output_str = 'It is a tie'
    else:
        return 'Server Error', 500

    return {
        'player' : player,
        'computer' : computer,
        'resutl_id' : match_output,
        'result' : match_output_str
    }

def main():
    """
    Function to setart the rest api
    """
    APP.add_api('api.yaml')
    serve(APP.app, listen='*:8080')

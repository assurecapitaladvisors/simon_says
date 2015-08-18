from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse

from .models import Game, generate_pattern

"""
User hits
/newgame POST
server responds with gameID
/game/<id>
browser would flash 1 color, user hits 1 color, browser sends POST /game/<id>
server compares POST data to sequence, responds with failure message or next
sequence
"""

# Create your views here.
def index(request):
    return HttpResonse("Here I am ")

@login_required
def newgame(request):
    game = Game()
    game.sequence = generate_pattern()
    game.save()
    return HttpResponse("I made a new game!")


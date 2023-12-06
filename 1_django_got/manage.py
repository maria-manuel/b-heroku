from django.urls import path
from django.http import HttpResponse, HttpResponseRedirect


def index(request):
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>Game of Thrones Fan Page</h1>
        <a href="/my-favorite-characters">My favorite GoT characters</a> <br />
        <a href="/top-episodes">Top GoT Episodes</a> <br />
    ''')


def characters(request):
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>My favorite Game of Thrones Characters</h1>
        <ul>
            <li>Daenerys Targaryen</li>
            <li>Jon Snow</li>
            <li>Tyrion Lannister</li>
            <li>Arya Stark</li>
        </ul>
        <hr />
        <a href="/">Back to home page</a>
    ''')


def favorite_episodes(request):
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>Top 3 episodes</h1>
        <ol>
            <li>Season 2 Episode 9: Blackwater</li>
            <li>Season 3 Episode 9: The Rains of Castamere</li>
            <li>Season 4 Episode 9: The Watchers on the Wall</li>
        </ol>
        <hr />
        <a href="/">Back to home page</a>
    ''')

def house_voting(request):
    print('voting page getting visited')
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h1>Vote for your favorite Game of Thrones house</h1>
        <a href="/vote/house-stark">House Stark: Winter is coming!</a> <br/>
        <a href="/vote/house-lannister">House Lannister: Hear me roar!</a> <br/>
        <a href="/vote/house-targaryen">House Targaryen: Fire and blood!</a> <br/>
        <hr />
        <a href="/">Back to home page</a>
    ''')

def vote_stark(request):
    print('house stark is getting a vote')
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h2>Your vote was recorded</h2>
        <hr />
        <a href="/">Back to voting page</a>
    ''')

def vote_lannister(request):
    print('house lannister is getting a vote')
    return HttpResponse('''
        <link rel="stylesheet" href="https://unpkg.com/sakura.css/css/sakura-vader.css" />

        <h2>Your vote was recorded</h2>
        <hr />
        <a href="/">Back to voting page</a>
    ''')

urlpatterns = [
    path('', index),
    path('my-favorite-characters', characters),
    path('top-episodes', favorite_episodes),
    path('vote/', house_voting),
    path('vote/house-stark', vote_stark),
    path('vote/lannister', vote_lannister),
]



# Boilerplate -- Don't worry about understanding anything from here down
def main():
    import sys
    from django.conf import settings
    from django.core.management import execute_from_command_line

    settings.configure(
        DEBUG=True,
        ALLOWED_HOSTS=['*'],
        SECRET_KEY='rre1h#l@&z!zcbg',
        ROOT_URLCONF=sys.modules[__name__],
    )

    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()

from riotwatcher import RiotWatcher, ApiError

watcher = RiotWatcher('RGAPI-efb6684c-6516-485e-902a-1206410a5a85')
my_region = 'br1'

class Invocador:

    def __init__(self, nome):
        self.nome = nome

    def rank(self):
        me = watcher.summoner.by_name(my_region, str(self.nome))
        elo = watcher.league.by_summoner(my_region, me['id'])
        rank = elo[0]['tier']+' '+elo[0]['rank']

        return rank

from riotwatcher import RiotWatcher, ApiError

watcher = RiotWatcher('RGAPI-efb6684c-6516-485e-902a-1206410a5a85')
my_region = 'br1'
champions = watcher.data_dragon.champions('9.23.1',0)['data']

champions[]

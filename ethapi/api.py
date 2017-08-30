from decorator import decorator

import ethapi.eth as eth
import ethapi.exceptions as exceptions


@decorator
def miner_id_required(f, *args, **kwargs):
    """
    Decorator helper function to ensure some methods aren't needlessly called
    without a miner configured.
    """
    try:
        if args[0].miner_id is None:
            raise AttributeError('Parameter miner_id is required.')
    except AttributeError:
        raise AttributeError('Parameter miner_id is required.')

    return f(*args, **kwargs)


@decorator
def worker_id_required(f, *args, **kwargs):
    """
    Decorator helper function to ensure some methods aren't needlessly called
    without a worker configured.
    """
    try:
        if args[0].worker_id is None:
            raise AttributeError('Parameter worker_id is required.')
    except AttributeError:
        raise AttributeError('Parameter worker_id is required.')

    return f(*args, **kwargs)


def check_required_args(required_args, args):
    """
    Checks if all required_args have a value.
    :param required_args: list of required args
    :param args: kwargs
    :return: True (if an exception isn't raised)
    """
    for arg in required_args:
        if arg not in args:
            raise KeyError('Required argument: %s' % arg)
    return True


class Api(eth.Eth):
    """
    Base class that extends ethapi and defaults API methods to
    unimplemented.
    """
    def __init__(self, **kwargs):
        super(Api, self).__init__(**kwargs)

    # Default to unimplemented methods
    def get(self, **kwargs):
        raise exceptions.UnimplementedException


class PoolStats(Api):
    """
    /poolStats API endpoint
    """
    def __init__(self, **kwargs):
        super(PoolStats, self).__init__(**kwargs)

    def get(self, **kwargs):
        """
        https://api.ethermine.org/docs/#api-Pool-poolStats
        """
        return self._get('poolStats')


class NetworkStats(Api):
    """
    /networkStats API endpoint
    """
    def __init__(self, **kwargs):
        super(NetworkStats, self).__init__(**kwargs)

    def get(self, **kwargs):
        """
        https://api.ethermine.org/docs/#api-Pool-networkStat
        """
        return self._get('networkStats')


class Miner(Api):
    """
    /miner API endpoint
    """
    def __init__(self, **kwargs):
        super(Miner, self).__init__(**kwargs)

    @miner_id_required
    def get(self, miner_id=None, end=None):
        """
        https://api.ethermine.org/docs/#api-Miner
        """
        return self._get('miner/%s/%s' % (miner_id, end))

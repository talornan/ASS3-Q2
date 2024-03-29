import unittest

from colorama import Fore

INF = float('inf')


def find_max_valuation_index(max_player, valuations):
    max_valuation = -INF
    chosen_item = -1
    for i, valuation in enumerate(valuations[max_player]):
        if valuation and valuation > max_valuation:
            max_valuation = valuation
            chosen_item = i
    return [chosen_item, max_valuation]


def weighted_round_robin(rights: list[float], valuations: list[list[float]], y: float) -> list[list[float]]:
    """
    Implements a weighted round-robin scheduling algorithm for resource allocation.

    Args:
        rights (list[float]): List of weights representing the rights of each player.
        valuations (list[list[float]]): List of valuation lists for each player.
        y (float): Constant factor used in the allocation process.

    Returns:
        list[list[float]]: List representing the allocation schedule, where each sublist contains
                            details of the allocation (player, item, valuation).
    """
    num_of_players = len(valuations)
    num_of_items = len(valuations[0])
    players = [0] * num_of_players
    ans = []
    item_index = 0
    while item_index < num_of_items:
        max_priority, chosen_player = max(
            ((rights[p] / (players[p] + y) if (players[p] + y) != 0 else INF, p) for p in range(num_of_players)),
            key=lambda x: x[0]
        )
        [chosen_item, item_valuation] = find_max_valuation_index(chosen_player, valuations)
        ans.append([chosen_player + 1, chosen_item + 1, item_valuation])
        players[chosen_player] += 1
        print("player", chosen_player + 1, "takes item", chosen_item + 1, "with value", item_valuation)
        # Remove chosen item from players' valuation lists.
        for val_list in valuations:
            val_list[chosen_item] = None
        item_index += 1
    return ans



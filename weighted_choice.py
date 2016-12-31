from __future__ import print_function

from random import random


def weighted_choice(sequence, weights):
    """Returns an element from sequence with the probability
    corresponding to the weights. Length of seq and weights
    should be exact.

    Args:
        sequence (iterable): Sequence of elements.
        weights (iterable): Sequence of weights corresponding to
            each element.

    Returns:
        An element from the sequence.
    """

    # Generate a list of cumulative sum of weights.
    # Example: [0.1, 0.4, 0.2] -> [0.1, 0.5, 0.7]
    acculated_weight = 0.0
    cumulative_weights = list()
    cumulative_weights_append = cumulative_weights.append

    for weight in weights:
        acculated_weight += weight
        cumulative_weights_append(acculated_weight)

    # A random value between 0.0 and the sum of weights is
    # is used to select the weighted sequence. Greater is the
    # difference between the cumulative weights, greater are the
    # chances of it getting picked.

    chance = random() * sum(weights)
    start_value = 0.0

    for index, weight in enumerate(cumulative_weights):
        if start_value <= chance < weight:
            # Weights and sequence corespond.
            return sequence[index]
        start_value = weight

    # This function is guaranteed to produce a result as random()
    # will always produce a value less than 1.0. So, return at
    # the end.

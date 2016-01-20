def sort_scores(unordered_scores, highest_possible_score):

    scores_to_counts = [0] * (highest_possible_score+1)

    for score in unordered_scores:
        scores_to_counts[score] += 1

    sorted_scores = []

    for score, count in enumerate(scores_to_counts):

        for time in range(count):

            sorted_scores.append(score)

    return sorted_scores

    

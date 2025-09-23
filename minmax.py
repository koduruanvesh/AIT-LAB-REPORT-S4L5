def minimax(depth, nodeIndex, isMax, scores, alpha, beta, height):
    if depth == height:
        return scores[nodeIndex]

    if isMax:
        best = float('-inf')

        val = minimax(depth + 1, nodeIndex * 2, False, scores, alpha, beta, height)
        best = max(best, val)
        alpha = max(alpha, best)
        if beta <= alpha:
            return best

        val = minimax(depth + 1, nodeIndex * 2 + 1, False, scores, alpha, beta, height)
        best = max(best, val)
        alpha = max(alpha, best)
        return best

    else:
        best = float('inf')

        val = minimax(depth + 1, nodeIndex * 2, True, scores, alpha, beta, height)
        best = min(best, val)
        beta = min(beta, best)
        if beta <= alpha:
            return best

        val = minimax(depth + 1, nodeIndex * 2 + 1, True, scores, alpha, beta, height)
        best = min(best, val)
        beta = min(beta, best)
        return best


if __name__ == "__main__":
    scores = [3, 5, 6, 9, 1, 2, 0, -1]
    import math
    height = int(math.log2(len(scores)))
    print("The optimal value is:", minimax(0, 0, True, scores, float('-inf'), float('inf'), height))

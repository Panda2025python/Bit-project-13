def stair_ways(n):
    if n == 0:
        return 1
    if n < 0:
        return 0
    return stair_ways(n - 1) + stair_ways(n - 2)


def generate_braces(current, open_count, close_count, total_pairs):
    if len(current) == total_pairs * 2:
        print(current)
        return

    if open_count < total_pairs:
        generate_braces(current + "{", open_count + 1, close_count, total_pairs)

    if close_count < open_count:
        generate_braces(current + "}", open_count, close_count + 1, total_pairs)


def make_grid(width, height):
    """
    create a grid that will hold all of the tiles
    for boggle game
    """
    return {(row, col): ' ' for row in range(height)
        for col in range(width)}
    
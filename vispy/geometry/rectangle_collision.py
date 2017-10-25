
def _score_function(rectangles):
    """Calculate the score of a configuration of rectangles.
    The score is defined as the pairwise sum over the overlapping area 
    between the rectangles.

    Parameters
    ----------
    rectangles : list
        List of tuples [(x1, y1, x2, y2)] where 
        (x1, y1) and (x2, y2) are the corners of the rectangle,
        such that x1 < x2 and y1 < y2.

    Returns
    -------
    score: float
        The score of the rectangle configuration.
    """
    return sum(_overlap(rectangle1, rectangle2) for (i, rectangle1) in enumerate(rectangles) for rectangle2 in rectangles[i+1:])

def _overlap(rectangle1, rectangle2):
    x11, y11, x21, y21 = rectangle1
    x12, y12, x22, y22 = rectangle2
    xOverlap = max(0, min(x21, x22) - max(x11, x12))
    yOverlap = max(0, min(y21, y22) - max(y11, y12))
    return xOverlap * yOverlap

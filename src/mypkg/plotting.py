import matplotlib.pyplot as plt

def plot_words(word_counts, n=10):
    """
    Plot a bar chart of the most common words and their counts.

    Parameters:
    word_counts (collections.Counter): A Counter object where keys are words and values are their counts.
    n (int): The number of top words to display in the bar chart. Defaults to 10.

    Returns:
    matplotlib.figure.Figure: The matplotlib Figure object containing the bar chart.

    Raises:
    ValueError: If `n` is not a positive integer.

    Example:
    >>> from collections import Counter
    >>> word_counts = Counter({'apple': 4, 'banana': 2, 'cherry': 7})
    >>> fig = plot_words(word_counts, n=3)
    """
    # Validate that n is a positive integer
    if not isinstance(n, int) or n <= 0:
        raise ValueError("The number of top words (n) must be a positive integer.")

    # Get the top n most common words and their counts
    top_n_words = word_counts.most_common(n)
    word, count = zip(*top_n_words)

    # Create the bar chart
    fig = plt.figure()
    plt.bar(range(n), count)
    plt.xticks(range(n), labels=word, rotation=45)
    plt.xlabel("Word")
    plt.ylabel("Count")
    
    return fig